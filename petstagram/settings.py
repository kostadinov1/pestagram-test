import os
from pathlib import Path
from decouple import config

APP_ENVIRONMENT = config('APP_ENVIRONMENT')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

# DEBUG = os.getenv('DEBUG', 'False') == 'True'
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', '127.0.0.1').split(' ')


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

)

THIRD_PARTY_APPS = ()

PROJECT_APPS = (
    'petstagram.main',
    'petstagram.accounts',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'petstagram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'petstagram.wsgi.application'


DATABASES = None
if APP_ENVIRONMENT == 'Production':
    DEFAULT_DATABASE_CONFIG = {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
    }

    DATABASES = {
        'default': DEFAULT_DATABASE_CONFIG,
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'petstagram',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': '127.0.0.1',
            'PORT': '5432',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'mediafiles'
MEDIA_URL = '/media/'

MEDIA_DIRS = [
    BASE_DIR / 'mediafiles'
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATE_DIRS = (
    os.path.join('settings.py', 'main'),
)

AUTH_USER_MODEL = 'accounts.PetstagramUser'
