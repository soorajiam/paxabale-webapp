from .base import config

STRIPE_PUBLIC_KEY = config.get('stripe', 'PUBLIC_KEY')
STRIPE_SECRET_KEY = config.get('stripe', 'SECRET_KEY')
STRIPE_WEBHOOK_SECRET = config.get('stripe', 'WEBHOOK_SECRET')