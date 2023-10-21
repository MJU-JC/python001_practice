"""
Django settings for dj2 project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from util.configread import config_read

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w5yn#0gn2tt7pvu%hvwt0!lt=!$6+eqp4%m8)u3u#gknm@jm)k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "main",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',#Forbidden (CSRF cookie not set.)
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'threadlocals.middleware.ThreadLocalMiddleware',
    "xmiddleware.xparam.Xparam",
    "xmiddleware.xauth.Xauth",

]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_COOKIE_NAME  = "sessionid"
SESSION_COOKIE_PATH  = "/"
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = False

ROOT_URLCONF = 'dj2.urls'
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'dj2.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'yclw9@qq.com'
EMAIL_HOST_PASSWORD = 'mhbrkuayvkkgbijd'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

dbtype, host, port, user, passwd, dbName, charset = config_read("config.ini")
dbName=dbName.replace(" ","").strip()
print(dbtype, host, port, user, passwd, dbName, charset)

if dbtype == 'mysql':
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'sql_mode': 'traditional',
                'init_command': "SET sql_mode='traditional'",  # STRICT_TRANS_TABLES
            },
            'NAME': dbName,
            'USER': user,
            'PASSWORD': passwd,
            'HOST': host,
            'PORT': port,
            'charset': charset,
            'TEST': {
                'CHARSET': charset,
                'COLLATION': 'utf8_general_ci',
            },
            'CONN_MAX_AGE':60
        },
    }
else:
    print("请使用mysql5.5数据库")
    os._exit(1)
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/



STATIC_URL = '/assets/'
STATICFILES_DIRS =[
os.path.join(BASE_DIR, "templates/front/assets"),
]

# media
MEDIA_URL = "/media/"  # 自定义
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 自定义
if os.path.isdir(MEDIA_ROOT) == False:
    os.mkdir(MEDIA_ROOT)