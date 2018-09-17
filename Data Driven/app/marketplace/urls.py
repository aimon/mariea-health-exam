from django.urls import path
from . import views

app_name = 'marketplace'

"""
1. View all plans available with the details above  - 'plan/'
2. Instantiate new carts                            - 'user/<int:pk>/cart_item/' or 'user/<int:pk>/cart/'
3. Add items to the carts                           - 'user/<int:pk>/cart_item/' or 'user/<int:user_id>/cart/<int:pk>/'
4. Change the count of an item in a cart            - 'user/<int:user_id>/cart/<int:pk>/cart_item/<int:pk>'
5. Remove an item from the cart                     - 'user/<int:user_id>/cart/<int:pk>/cart_item/<int:pk>'
6. See the items in a cart                          - 'user/<int:user_id>/cart/<int:pk>/cart_item'
7. Pay for the cart                                 - 'cart/<int:pk>/paid' or 'user/<int:user_id>/cart/<int:pk>/'
    - Just create an endpoint that when invoked, automatically marks the cart as paid
"""
urlpatterns = [
    # Provider's CRUD
    path('provider/', views.ProviderListCreate.as_view()),
    path('provider/<int:pk>/', views.ProviderRetrieveUpdateDestroy.as_view()),

    # Payment Term's CRUD
    path('payment_term/', views.PaymentTermListCreate.as_view()),
    path('payment_term/<int:pk>/', views.PaymentTermRetrieveUpdateDestroy.as_view()),

    # Plan's CRUD
    path('plan/', views.PlanListCreate.as_view()),
    path('plan/<int:pk>/', views.PlanRetrieveUpdateDestroy.as_view()),

    # Plan Term's CRUD - this is where all the plan prices are located
    path('plan_term/', views.PlanTermListCreate.as_view()),
    path('plan_term/<int:pk>/', views.PlanTermRetrieveUpdateDestroy.as_view()),

    # User's CRUD
    path('user/', views.UserListCreate.as_view()),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view()),

    # 1. There's only one active cart at a time
    # 2. Cart must be updated to paid to be able to instantiate new cart
    # 3. but Cart can also be updated using this 'user/<int:pk>/cart/' endpoint

    # User's Cart List/Create View
    path('user/<int:pk>/cart/', views.CartListCreate.as_view()),


    # User's Cart View (specific cart)
    path('user/<int:user_id>/cart/<int:pk>/', views.CartRetrieveUpdateDestroy.as_view()),


    # User's Cart Items
    path('user/<int:user_id>/cart/<int:pk>/cart_item/', views.CartItemListCreate.as_view()),
    path('user/<int:user_id>/cart/<int:cart_id>/cart_item/<int:pk>/', views.CartItemRetrieveUpdateDestroy.as_view()),

    # 1. This 'user/<int:pk>/cart_item/' endpoint can automatically create Cart if not yet exists
    # 2. Duplicate plan/plan_term will add the value of current plus the entered quantity

    # User's Add to Cart Function
    path('user/<int:pk>/cart_item/', views.CartItemAdd.as_view()),

    # Mark Cart as Paid
    path('cart/<int:pk>/paid', views.CartPaid.as_view()),

]
