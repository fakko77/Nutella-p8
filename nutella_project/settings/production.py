from . import *
SECRET_KEY = '$)6%isi2^)8hntw2yee&mp7b%pql9@nyg907x17j*&x07gl&_r'
DEBUG = False
ALLOWED_HOSTS = ['68.183.25.236']
DATABASES = {
            'default': {
                 'ENGINE': 'django.db.backends.postgresql_psycopg2',
                 'NAME': 'nutella',
                 'USER': 'morgan',
                 'PASSWORD': 'ty',
                 'HOST': 'localhost',
                 'PORT': '5432',
                 }
            }



