from django.urls import path
from . import views

urlpatterns = [
    # Existing Stripe paths
    path('/stripe/create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('/stripe/webhook/', views.stripe_webhook, name='stripe-webhook'),
    path('/stripe/subscriptions/', views.list_subscriptions, name='list-subscriptions'),
    path('customer-subscription/', views.get_customer_subscription, name='customer-subscription'),
    path('cancel-subscription/', views.cancel_subscription, name='cancel-subscription'),
    path('payment-history/', views.payment_history, name='payment-history'),
    path('list-plans/', views.list_plans, name='list-plans'),
    
    # New Razorpay paths
    path('razorpay/create-order/', views.create_razorpay_order, name='create-razorpay-order'),
    path('razorpay/verify-payment/', views.verify_razorpay_payment, name='verify-razorpay-payment'),
    path('razorpay/create-subscription/', views.create_razorpay_subscription, name='create-razorpay-subscription'),
    path('razorpay/verify-subscription/', views.verify_razorpay_subscription, name='verify-razorpay-subscription'),
    path('razorpay/webhook/', views.razorpay_webhook, name='razorpay-webhook'),
    path('razorpay/subscriptions/', views.list_razorpay_subscriptions, name='list-razorpay-subscriptions'),
    path('razorpay/cancel-subscription/', views.cancel_razorpay_subscription, name='cancel-razorpay-subscription'),
]