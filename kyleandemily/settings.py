"""
Django settings for kyleandemily project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'kyleandemily')
DB_ROOT = '/Volumes/STORAGE/Database/kyleandemily'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ldfcujr4!-fnh1czol@+!t#h1hh)56@%)@k$*hz36wwokkw!m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['www.kyleandemily.com',
                 'kyleandemily.com',
                 'media.kyleandemily.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'kyleandemily.wedding',
    'kyleandemily.base',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kyleandemily.urls'

WSGI_APPLICATION = 'kyleandemily.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'http://media.kyleandemily.com/'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates')
)

try:
    from kyleandemily.local_settings import *
except ImportError:
    pass

#This needs to come after the local_settings import so we can override the DB_ROOT var
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'deafult.db'),
    },
    'wedding': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'wedding.db'),
    }
}