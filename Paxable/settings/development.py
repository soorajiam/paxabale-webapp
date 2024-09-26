from .base import *
import sys
import dj_database_url

import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False") == "True"
print('FRONTEND_URL: ', os.getenv('FRONTEND_URL', 'http://127.0.0.1:8000'))
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://127.0.0.1:8000')

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'dist'),
]

# Configure development database
# if DEVELOPMENT_MODE is True:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
# elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
#     if os.getenv("DATABASE_URL", None) is None:
#         raise Exception("DATABASE_URL environment variable not defined")
#     DATABASES = {
#         "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
#     }


# Email configuration for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

