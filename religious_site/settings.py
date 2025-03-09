import os
from pathlib import Path
import dj_database_url


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^7!o%%0@0k*ltv_esu6!qpdye9i=^hc09t3p==b$9cs0_6ge+v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False for production

ALLOWED_HOSTS = ['religious-site.onrender.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'whitenoise.runserver_nostatic',  # WhiteNoise for static file handling
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'religious_site.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Ensure templates are found
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'religious_site.wsgi.application'

# Database (SQLite for now, can change to PostgreSQL later)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'religious_site_db',  # Use your actual database name
        'USER': 'religious_site_db_user',  # Use your actual database user
        'PASSWORD': '9WUbYKuZ5cYcF1gUAirCi2eLWbJXMgHU',  # Use your actual password
        'HOST': 'dpg-cv4reoaj1k6c738qlc00-a.oregon-postgres.render.com',  # Only hostname
        'PORT': '5432',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Where collectstatic stores files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Additional static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
