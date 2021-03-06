# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #this points to the dir above this file
ROOT_PATH = os.path.dirname(__file__) #this points to the current dir


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nbb)vwwa+xo+ad%ss$a)e71fr4yr#&ag_7j5(gnmzt1sifsm13'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


ADMINS = (
    ('Robert Boyett', 'rdboyett@gmail.com'),
)
MANAGERS = ADMINS

ALLOWED_HOSTS = ['aisboard.alvaradoisd.net']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'directory_app',
    'google_login',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'directory_project.urls'

WSGI_APPLICATION = 'directory_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	    'NAME': 'directorydb',                      # Or path to database file if using sqlite3.
	    'USER': 'root',                      # Not used with sqlite3.
	    'PASSWORD': 'dallas20',                  # Not used with sqlite3.
	    'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
	    'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
	}
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_ROOT = '/var/www/aisboard/static/'

STATIC_URL = '/static/'



TEMPLATE_DIRS = (os.path.join(ROOT_PATH,'templates'),)
STATICFILES_DIRS = (os.path.join(ROOT_PATH,'static'),)


LOGIN_URL          = '/google/auth/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_ERROR_URL    = '/google/error/'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rboyett@alvaradoisd.net'
EMAIL_HOST_PASSWORD = 'dallas20'
EMAIL_PORT = 587
EMAIL_USE_TLS = True



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


'''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S",
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}


'''








