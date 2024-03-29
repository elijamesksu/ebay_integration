# ebay_integration/settings.py
import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import logging

BASE_DIR = Path(__file__).resolve().parent.parent
# Path to the log file
LOG_FILE_PATH = BASE_DIR / 'debug.log'

SECRET_KEY = 'x5dv)8o+%33c)t3j6y_747-gi*$9!%s1rh!9(p=f*#dztmoiu+'
DEBUG = True

ALLOWED_HOSTS = ['ebay-integration-b1dc507216da.herokuapp.com', 'localhost', '127.0.0.1', 'rapidresaledemo.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ebay_oauth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ebay_integration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ebay_integration.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Create a logger object
logger = logging.getLogger(__name__)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# eBay OAuth configurations
EBAY_CLIENT_ID = 'RapidRes-RapidRes-PRD-083448d6e-7b744566'
EBAY_CLIENT_SECRET = 'PRD-83448d6ee35b-1b2d-49aa-9f3f-2811'
EBAY_REDIRECT_URI = 'https://ebay-integration-b1dc507216da.herokuapp.com/ebay/callback/'
EBAY_RU_NAME = 'RapidResale_Co-RapidRes-RapidR-soucmz'
STATIC_ROOT = BASE_DIR / 'staticfiles'
