from os import environ
import logging
from os.path import (join, dirname, abspath)

from django.utils.translation import ugettext_lazy as T

from dotenv import load_dotenv


BASE_DIR = dirname(dirname('__file_'))
BASE_PATH = dirname(BASE_DIR)
load_dotenv(join(BASE_PATH, '.env'))

DEV_ENV = int(environ.get("DEV_ENV"))

SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = DEV_ENV
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'talaikis.com', 'www.talaikis.com']
ALLOWED_API_DOMAINS = ALLOWED_HOSTS + ['codepen.io']
STATIC_ROOT = '{}static'.format(BASE_DIR)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'redir',
    'rest_framework',
    'ckeditor',
]

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Custom': [
            {'name': 'basic', 'items': [
                'Styles','Format','Font','FontSize' '-', 'Bold', 'Italic', 'Underline', 'Superscript',
                'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'Table',
                'Link', 'Unlink', 'SpellChecker',
                'RemoveFormat', 'Source', 'CodeSnippet'
            ]}
        ],
        'codeSnippet_theme': 'railscasts',
         'codeSnippet_languages': {
             'python': 'Python',
             'javascript': 'JavaScript',
             'golang': 'Golang',
             'sql': 'SQL',
         },
        'toolbar': 'Custom',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]),
    }
}

MIDDLEWARE = [
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sekmet.urls'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

#REST_FRAMEWORK = {
#    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#    'PAGE_SIZE': 100
#}

if not DEV_ENV:
    CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                'LOCATION': '127.0.0.1:11211',
                #LOCATION': [
                    #'172.19.26.240:11211',
                    #'172.19.26.242:11211',
                #]
                #'LOCATION': 'unix:/tmp/memcached.sock',
                'TIMEOUT': 10000, #3 hours
                #'OPTIONS': {
                    #'MAX_ENTRIES': 20000
                #}
            }
        }

    CACHE_MIDDLEWARE_KEY_PREFIX = 'tlsk'
    CACHE_MIDDLEWARE_SECONDS = 21600

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'sekmet.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', T('English')),
    ('lt', T('Lietuvių')),
)

LOCALE_PATHS = (
    join(BASE_DIR, 'locale'),
)

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': join(BASE_DIR, 'logs', 'django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

DEFAULT_FROM_EMAIL = environ.get("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

environ.get("SECRET_KEY")

EMAIL_HOST = environ.get("EMAIL_HOST")
EMAIL_HOST_USER = environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 2525
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_NOREPLY = environ.get("EMAIL_NOREPLY")
#EMAIL_SSL_KEYFILE = 'C:\\nginx\\conf\\certs\\privkey.pem'
#EMAIL_SSL_CERTFILE = 'C:\\\nginx\\conf\\certs\\cert.pem'
NOTIFICATIONS_EMAILS = [environ.get("NOTIFICATIONS_EMAILS")]
NOTIFICATIONS_ENABLED = True
