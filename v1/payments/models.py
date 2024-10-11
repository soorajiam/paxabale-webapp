from django.db import models
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCustomer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)

    @classmethod
    def get_or_create(cls, user):
        stripe_customer, created = cls.objects.get_or_create(user=user)
        if created:
            customer = stripe.Customer.create(email=user.email)
            stripe_customer.stripe_customer_id = customer.id
            stripe_customer.save()
        return stripe_customer

class RazorpayCustomer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    razorpay_customer_id = models.CharField(max_length=255, blank=True, null=True)

class Plan(models.Model):
    name = models.CharField(max_length=100)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_plan_id = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    interval = models.CharField(max_length=20, choices=[('month', 'Monthly'), ('year', 'Yearly')], default='month')
    description = models.TextField(blank=True, null=True)

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, default='inactive')
    current_period_end = models.DateTimeField(null=True, blank=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_subscription_id = models.CharField(max_length=255, blank=True, null=True)

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.amount} - {self.status}"