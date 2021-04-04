"""
Django settings for opendata project.

Generated by 'django-admin startproject' using Django 3.2rc1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
from pathlib import Path
from kombu import Exchange, Queue

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))


def path(args):
    return os.path.join(PROJECT_PATH, args)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w$uvf!t1jj61%uxl(r4ap!=ac1xm16kqj*g2c%8-&0az3@lc)#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PRODUCTION = False

ALLOWED_HOSTS = []

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.humanize',
    'django.contrib.gis',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_gis',
    'drf_yasg',
    'django_filters',
    'django_celery_results',
    'django_celery_beat',
]

LOCAL_APPS = [
    'data'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'opendata.urls'

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

WSGI_APPLICATION = 'opendata.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE',
                                 'django.contrib.gis.db.backends.postgis'),
        'NAME': os.environ.get('DB_NAME', 'opendata'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_ROOT = os.environ.get('STATIC_ROOT', 'static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    path('/usr/local/lib/python3.6/dist-packages/django/contrib/admin/static'),
)

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', 'media/')

MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (

    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DATETIME_FORMAT': 'iso-8601',
    'DATETIME_INPUT_FORMATS': ['iso-8601', '%Y-%m-%d %H:%M:%S'],
    'DATE_FORMAT': '%Y-%m-%d',
    'DATE_INPUT_FORMATS': ['iso-8601'],
    'TIME_FORMAT': '%H:%M:%S',
    'TIME_INPUT_FORMATS': ['iso-8601'],
    'COERCE_DECIMAL_TO_STRING': False,
}

# Celery
CELERY_BROKER_URL = 'pyamqp://guest@localhost//'

CELERY_RESULT_PERSISTENT = True

CELERY_RESULT_BACKEND = 'django-db'

CELERY_IMPORTS = [
    'data.tasks'
]

CELERY_QUEUES = (
    Queue('tasks', exchange=Exchange('tasks', type='direct'))
)

CELERY_TIMEZONE = TIME_ZONE

SWAGGER_URL = os.environ.get('SWAGGER_URL')

try:
    from .local_settings import *
except:
    pass
