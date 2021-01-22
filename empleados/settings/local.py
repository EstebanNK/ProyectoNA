from .base import*

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'esteban',
        'PASSWORD': 'curso',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.parent / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'