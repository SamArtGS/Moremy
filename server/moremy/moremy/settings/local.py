from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": get_secret("DB_NAME"),  # Nombre de la base de datos
    "USER": get_secret("USER"),
    "PASSWORD": get_secret("PASSWORD"),
    "HOST": "moremydb.c7rbflvluzyk.us-east-2.rds.amazonaws.com",
    "PORT": "3306",  # Puerto por defecto de MySQL
  }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR.child("static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.child("media")
