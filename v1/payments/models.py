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

class Plan(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0.00)
    interval = models.CharField(max_length=20, choices=[('month', 'Monthly'), ('year', 'Yearly')], default='month')
    description = models.TextField(blank=True, null=True)

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, default='inactive')
    current_period_end = models.DateTimeField(null=True, blank=True)

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True)