"""
Django settings for tutorias project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=2vpy+*r3q1584d7&ylkrirhr0utn*sro$g612qbrfhm(6zgt+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #APLICACIONES EXTRAS
    'usuarios',
    'generales'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tutorias.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'usuarios.context_processors.user_info',

            ],
        },
    },
]

WSGI_APPLICATION = 'tutorias.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
AUTH_USER_MODEL = 'usuarios.CustomUser'



JAZZMIN_SETTINGS = {
  # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "STP",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "STP",
    "site_brand": "STP",

    # Logo to use for your site, must be present in static files, used for brand on top left

    "welcome_sign": "Bienvenido al Sistema STP",

    "changeform_format": "single",


    'icons':{
        "comedor.TipoDieta": 'fas fa-carrot',
        "comedor.Dietas": 'fas fa-leaf',
        "comedor.Comedor": 'fas fa-chair',
        "comedor.BoxLunch": 'fas fa-box-open',

        'auth.user': "fas fa-user",
        'auth.group': "fas fa-users",
        "acuerdoinicio.TestigoUno": 'fas fa-eye',
        "acuerdoinicio.TestigoDos": 'fas fa-eye',
        "acuerdoinicio.Traductor": 'fas fa-language',
        "catalogos.Tipos": 'fas fa-tags',
        "catalogos.Estatus": 'fas fa-check',
        "catalogos.Estado": 'fas fa-flag',
        "catalogos.Responsable": 'fas fa-user',
        "catalogos.Estacion": 'fas fa-subway',
        "comparecencia.comparecencia": 'fas fa-gavel',
        "generales.ImagenCarrousel": 'fas fa-image',
        "pertenencias.Inventario": 'fas fa-archive',
        "pertenencias.Pertenencias": 'fas fa-briefcase',
        "pertenencias.Valores": 'fas fa-coins',
        "salud.ExpedienteMedico": 'fas fa-notes-medical',
        "usuarios.Usuario": 'fas fa-user',
        
    }

}


