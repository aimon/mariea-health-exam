from django.db import models
from django.core.validators import MinLengthValidator


class Provider(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PaymentTerm(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    provider = models.ForeignKey('marketplace.Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], unique=True)
    description = models.CharField(max_length=500, validators=[MinLengthValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def plan_terms(self):
        return self.planterm_set.all()


class PlanTerm(models.Model):
    plan = models.ForeignKey('marketplace.Plan', on_delete=models.CASCADE)
    payment_term = models.ForeignKey('marketplace.PaymentTerm', on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('plan', 'payment_term',)

    def __str__(self):
        return self.plan.name + ' - ' + self.payment_term.name + ' (' + str(self.price) + ')'


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[MinLengthValidator(3)], unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class CartItem(models.Model):
    cart = models.ForeignKey('marketplace.Cart', on_delete=models.CASCADE, blank=True)
    plan = models.ForeignKey('marketplace.Plan', on_delete=models.CASCADE)
    plan_term = models.ForeignKey('marketplace.PlanTerm', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Cart(models.Model):
    STATUS_NOT_YET_PAID = 'not_yet_paid'
    STATUS_PAID = 'paid'
    STATUSES = (
        (STATUS_NOT_YET_PAID, 'Not yet paid'),
        (STATUS_PAID, 'Paid')
    )
    user = models.ForeignKey('marketplace.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=12, default=STATUS_NOT_YET_PAID, choices=STATUSES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Cart ID# ' + str(self.pk) + ' (' + self.status + ')'

    def cart_items(self):
        return self.cartitem_set.all()
