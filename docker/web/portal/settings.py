import os
from datetime import timedelta

import environ

# указываем главной директорией папку web
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# подгружаем переменные среды из файла cust.env
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

global_variables = {}
global_variables['DEBUG'] = DEBUG

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1/*", f"http://{env('LOCAL_IP')}/*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'ckeditor',
    'ckeditor_uploader',
    'multiselectfield',
    'apps.websocket',
    'apps.logging',
    'apps.chat',
    'apps.wiki',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'portal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    },
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = env('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR + '/static'
MEDIA_ROOT = BASE_DIR + '/media'


#############################################
# WEBSOCKETS (CHANNELS)                     #
#############################################

ASGI_APPLICATION = "portal.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}


#############################################
# CLICKHOUSE                                #
#############################################

CLICKHOUSE_REDIS_CONFIG = {
    'host': 'redis',
    'port': 6379,
    'db': 8,
    'socket_timeout': 10,
}

CLICKHOUSE_CELERY_QUEUE = 'clickhouse'


CELERYBEAT_SCHEDULE = {
    'clickhouse_auto_sync': {
        'task': 'django_clickhouse.tasks.clickhouse_auto_sync',
        'schedule': timedelta(seconds=2),  # Every 2 seconds
        'options': {'expires': 1, 'queue': CLICKHOUSE_CELERY_QUEUE},
    },
}


#############################################
# CKEDITOR                                  #
#############################################

CKEDITOR_BASEPATH = STATIC_URL + "ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'office2013',
        'toolbar': 'None',
        'height': '800px',
        'width': '110%',
        # 'extraPlugins': 'dialog,div',
    },

}
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'


#############################################
# LDAP                                      #
#############################################

AUTHENTICATION_BACKENDS = (
    # 'apps.security.auth.ldap', #добавил самописную аутентификацию\регистрацию по ldap
    'django.contrib.auth.backends.ModelBackend',
    )

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
