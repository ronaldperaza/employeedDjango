from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'ronald',
        'PASSWORD': 'empleadopassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
        # 'NAME': BASE_DIR / 'db.sqlite3',

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#ARCHIVO DE CONFIGURACION y guardado DE ARCHIVOS ESTATICOS
STATICFILES_DIRS = [BASE_DIR.child('static')]


