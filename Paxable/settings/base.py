from pathlib import Path
from datetime import timedelta
import os
from configparser import RawConfigParser



config = RawConfigParser()
config.read('/etc/secret/opentranslate/local.ini')

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config.get('app', 'SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken', 
     'drf_yasg',
   
    "corsheaders",
    'core',
     'v1.authentication',
    'v1.payments',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'Paxable.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'dist')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Paxable.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

WHITENOISE_USE_FINDERS = True

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

AUTH_USER_MODEL = 'authentication.CustomUser'

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'my-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'REGISTER_SERIALIZER': 'authentication.serializers.CustomRegisterSerializer',
    'LOGIN_SERIALIZER': 'authentication.serializers.CustomLoginSerializer',
    'USER_DETAILS_SERIALIZER': 'authentication.serializers.CustomUserDetailsSerializer',
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ORIGIN_WHITELIST = [
     "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-disposition',
    'content-type',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'user-id',
    'bearer',
    'node-id',
    'otp',
    'timezone',
    'language'
]
CORS_PREFLIGHT_MAX_AGE = 86400
CORS_ALLOW_CREDENTIALS = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config.get('email', 'HOST_NAME')
EMAIL_PORT = int(config.get('email', 'PORT'))  # Convert to integer
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config.get('email', 'EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_PASSWORD')

# Default from email
DEFAULT_FROM_EMAIL = 'hello@opentranslate.dev'

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'api/auth/registration/verify-email//'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'api/auth/registration/verify-email/'

STRIPE_PUBLIC_KEY = config.get('stripe', 'PUBLIC_KEY')
STRIPE_SECRET_KEY = config.get('stripe', 'SECRET_KEY')
STRIPE_WEBHOOK_SECRET = config.get('stripe', 'WEBHOOK_SECRET')

# Add these lines for debugging email issues
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = 30  # in seconds
DEBUG = True  # Set to False in production

GOOGLE_OAUTH2_CLIENT_ID = config.get('google', 'CLIENT_ID', fallback="")
GOOGLE_OAUTH2_CLIENT_SECRET = config.get('google', 'CLIENT_SECRET', fallback="")
GOOGLE_OAUTH2_REDIRECT_URI = config.get('google', 'REDIRECT_URI', fallback="")
