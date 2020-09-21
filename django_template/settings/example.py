from django_template.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
# generate for example at https://djecrety.ir
SECRET_KEY = '--insert secret key here--'

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}