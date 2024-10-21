from .settings import *
from dotenv import dotenv_values

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
config  = dotenv_values(".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', "192.168.0.21"]




# Application definition
#'rest_framework_simplejwt',
INSTALLED_APPS = [
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken", # Add
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example'
]

CORS_ALLOWED_ORIGINS = [
    "http://192.168.0.21:3000",  # URL do seu frontend (ajuste conforme necessário)
    "http://localhost:3000",
]

CORS_ALLOW_ALL_ORIGINS = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Note: Django modules for using databases are not support in serverless
# environments like Vercel. You can use a database over HTTP, hosted elsewhere.
DATABASES = {
    'default': {
        'ENGINE': config["PG_ENGINE"],
        'NAME': config["PG_NAME"],
        'USER': config["PG_USER"],
        'PASSWORD': config["PG_PASSWORD"],
        'HOST': config["PG_HOST"],
        'PORT': config["PG_PORT"],
    }
}


CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True




