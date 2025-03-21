from datetime import timedelta
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent



DATABASES = {
   'default': {
       'ENGINE': os.getenv("DB_ENGINE"),
       'NAME': os.getenv("DB_DATABASE"),
       'USER': os.getenv("DB_USERNAME"),
       'PASSWORD': os.getenv("DB_PASSWORD"),
       'HOST': os.getenv("DB_HOST"),
       'PORT':  os.getenv("DB_PORT"),
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["http://127.0.0.1:8000/"]
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000/"]


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'accounts',
    'exam',
    "core",
    "markethub",
    "django_celery_results",
    'django_celery_beat',
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

ROOT_URLCONF = 'olfati_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'olfati_django.wsgi.application'

AUTH_USER_MODEL = 'accounts.UserModel'


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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,  
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PAYLOAD_HANDLER': 'path.to.custom_payload_handler', 
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'path.to.custom_response_payload_handler',
    
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(weeks=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=48), 
}

REDIRECTURL = "https://olfati.iran.liara.run"
CALLBACKURL = 'http://{REDIRECTURL}/markethub/zarrin-pall/verify/'
MERCHANT= os.getenv('MERCHANTY')

LANGUAGE_CODE = 'fa'




