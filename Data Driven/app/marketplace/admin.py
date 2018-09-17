from django.contrib import admin
from .models import Provider, PaymentTerm, Plan, PlanTerm, User, Cart, CartItem

# Register your models here.
admin.site.register(Provider)
admin.site.register(PaymentTerm)
admin.site.register(Plan)
admin.site.register(PlanTerm)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(CartItem)

