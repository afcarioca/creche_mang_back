from .settings import *
import os
from dotenv import load_dotenv
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


##SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=cldztbc4jg&xl0!x673!*v2_=p$$eu)=7*f#d0#zs$44xx-h^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Note: Django modules for using databases are not support in serverless
# environments like Vercel. You can use a database over HTTP, hosted elsewhere.

DATABASES = {}









