# your_project/settings.py

import os
from pathlib import Path
import environ

# ─── BASE DIR ────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── ENVIRONMENT VARIABLES ───────────────────────────────────────────────────
env = environ.Env(
    DEBUG=(bool, False)
)
# read .env file at project root
environ.Env.read_env(env_file=str(BASE_DIR / '.env'))

SECRET_KEY       = env('SECRET_KEY')
DEBUG            = env('DEBUG')
ALLOWED_HOSTS    = env.list('ALLOWED_HOSTS', default=[])

# ─── INSTALLED APPS ─────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Travel_App',
]

# ─── MIDDLEWARE ──────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',        # <— add Whitenoise here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ─── URL / WSGI ──────────────────────────────────────────────────────────────
ROOT_URLCONF  = 'TravelTogether.urls'
WSGI_APPLICATION = 'TravelTogether.wsgi.application'

# ─── DATABASE ────────────────────────────────────────────────────────────────
# expects DATABASE_URL=mysql://user:pass@host:port/name
DATABASES = {
    'default': env.db()
}

# ─── TEMPLATES ───────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],    # or [BASE_DIR / 'templates'] if you have a top-level templates dir
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

# ─── INTERNATIONALIZATION ────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_TZ        = True

# ─── STATIC FILES (CSS, JS, IMAGES) ─────────────────────────────────────────
STATIC_URL           = '/static/'
STATIC_ROOT          = BASE_DIR / 'staticfiles'
STATICFILES_DIRS     = [ BASE_DIR / 'Travel_App' / 'static' ]
STATICFILES_STORAGE  = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ─── MEDIA UPLOADS ───────────────────────────────────────────────────────────
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ─── DEFAULT PK FIELD TYPE ──────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
