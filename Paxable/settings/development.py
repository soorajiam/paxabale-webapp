from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'dist'),
]

# Configure development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Email configuration for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FRONTEND_URL = 'http://127.0.0.1:8000'

