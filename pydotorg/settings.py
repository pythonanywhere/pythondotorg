import os
import dj_database_url

### Basic config

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DEBUG = TEMPLATE_DEBUG = True
SITE_ID = 1
SECRET_KEY = 'hu9h&&%j*tcj2o9!k2w%ao=fcw&$0z$)la$&8vl+s$4y%r946h'

### Databases

DATABASES = {
    'default': dj_database_url.config(default='postgres:///python.org')
}

### Locale settings

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

### Files (media and static)

MEDIA_ROOT = os.path.join(BASE, 'media')
MEDIA_URL = '/m/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE, 'static-root')
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE, 'static'),)

### Templates

TEMPLATE_DIRS = [
    os.path.join(BASE, 'templates')
]

### URLs, WSGI, middleware, etc.

ROOT_URLCONF = 'pydotorg.urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

WSGI_APPLICATION = 'pydotorg.wsgi.application'

### Apps

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'south',

    'boxes',
    'cms',
    'pages',
)

### Testing

TEST_RUNNER = 'discover_runner.DiscoverRunner'

### Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}