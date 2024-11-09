from .settings import *
import os
#from dotenv import dotenv_values

#from dotenv import load_dotenv
#load_dotenv()
#config  = dotenv_values(".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


##SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
#SECRET_KEY = config["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

# Application definition
INSTALLED_APPS = [
    "rest_framework.authtoken", # Add
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example',
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Note: Django modules for using databases are not support in serverless
## environments like Vercel. You can use a database over HTTP, hosted elsewhere.


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_VERCEL_DATABASE"),
        'USER': os.environ.get("POSTGRES_VERCEL_USER"),
        'PASSWORD': os.environ.get("POSTGRES_VERCEL_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_VERCEL_HOST"),
        'PORT': "5432",
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': config["POSTGRES_VERCEL_ENGINE"],
        'NAME': config["POSTGRES_VERCEL_DATABASE"],
        'USER': config["POSTGRES_VERCEL_USER"],
        'PASSWORD': config["POSTGRES_VERCEL_PASSWORD"],
        'HOST': config["POSTGRES_VERCEL_HOST"],
        'PORT': config["POSTGRES_VERCEL_PORT"],
    }
}
'''















