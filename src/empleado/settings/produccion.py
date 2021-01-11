from .base import *

DEBUG = True

ALLOWED_HOSTS = ['employedd.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6l16pi6naat5a',
        'USER': 'upebngfhhdmehr',
        'PASSWORD': '49c644118261377c9a5992b93ec9c4e2e1ee867fa0ee36fcc5a00796caccc846',
        'HOST': 'ec2-18-235-107-171.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
        # 'NAME': BASE_DIR / 'db.sqlite3',

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#ARCHIVO DE CONFIGURACION y guardado DE ARCHIVOS ESTATICOS
STATICFILES_DIRS = [BASE_DIR.child('static')]

#archivos multimesdia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


