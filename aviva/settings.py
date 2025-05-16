from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production!
# Remove this line since it's duplicated
# SECRET_KEY = 'django-insecure-dp(drwrqe_o=f*1uxr3meyv&*ra!kiko-ocv)jv**b@oclku9#'

# Keep only this one
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-key-for-development')

# SECURITY WARNING: don't run with debug turned on in production!
# Remove duplicate SECRET_KEY definition
# SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-key-for-development')

# Set DEBUG to False for production
DEBUG = False

ALLOWED_HOSTS = [
    'drharipriyasaesthetics.onrender.com',
    '*.onrender.com',
    'localhost',
    '127.0.0.1'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aviva.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'appointments', 'templates')],  # ✅ add if you want to support global templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aviva.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ✅ Static files (CSS, JavaScript, Images)
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Changed from 'appointments/static'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-key-for-development')

# ✅ Email setup (Gmail SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'gmallik1011@gmail.com'  # your email
EMAIL_HOST_PASSWORD = 'qchq yppl ljsr pzjr'  # app password, keep this secure


# ✅ CORS and CSRF settings (for local dev only, remove for production)
# CORS and CSRF settings
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5501",
    "https://drharipriyasaesthetics.onrender.com",
]
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5501",
    "https://drharipriyasaesthetics.onrender.com",
]

CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True  # Changed to True for production
SESSION_COOKIE_SECURE = True  # Changed to True for production

# Enable WhiteNoise compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appointments',
    'corsheaders',
]
DEBUG = True  # Temporarily set to True to see the error
