from django.urls import path
from . import views

urlpatterns = [
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('webhook/', views.stripe_webhook, name='stripe-webhook'),
    path('subscriptions/', views.list_subscriptions, name='list-subscriptions'),
    path('customer-subscription/', views.get_customer_subscription, name='customer-subscription'),
    path('cancel-subscription/', views.cancel_subscription, name='cancel-subscription'),
    path('payment-history/', views.payment_history, name='payment-history'),
    path('list-plans/', views.list_plans, name='list-plans'),
]