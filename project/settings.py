# coding: utf-8
import os
import environ
root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = root()

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db()
}

# public_root = root.path('public/')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
SECRET_KEY = env('SECRET_KEY')
LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'googlecharts'
]

LOCAL_APPS = [
    'apps.reports',
    'apps.profiles',
    'apps.accounts',
    'apps.frontend',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

# AUTH_USER_MODEL = 'accounts.User'
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates')
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'

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
