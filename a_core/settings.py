"""
Django settings for a_core project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s)ad*(qe-h#5n#^g1m7reyb07&3%fgk2#a7qfrfcusytp5h9*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # For multiple domain sites
    'django.contrib.sites',
    
    # allauth framework
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # third-part
    'django_htmx',
    
    # Created applications
    'a_posts',
    'a_users',
    'a_inbox',
    
    'django_cleanup.apps.CleanupConfig',
    
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",    
]

ROOT_URLCONF = 'a_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
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


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'a_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True

# ACCOUNT_USERNAME_BlACKLIST = ['admin', 'accounts', 'profile', 'category', 'post', 'delete', 'edit', 'inbox']

ACCOUNT_USERNAME_BLACKLIST = [
    # System and admin terms
    'admin', 'administrator', 'root', 'sysadmin', 'system', 'operator', 
    'support', 'service', 'helpdesk', 'help', 'info', 'contact', 'security', 
    'moderator', 'mod', 'staff', 'user', 'guest', 'superuser',

    # Generic names and placeholder terms
    'test', 'null', 'undefined', 'anonymous', 'unknown', 'public', 'official', 
    'nobody', 'somebody', 'anybody', 'someone',

    # Positions and roles
    'manager', 'director', 'developer', 'engineer', 'ceo', 'founder', 'cofounder', 
    'adminuser', 'supervisor', 'operator', 'moderator', 'supportstaff',

    # Brand and project-related terms (replace 'yourbrand' with your brand name)
    'yourbrand', 'yourbrandadmin', 'yourbrandteam', 'official', 'yourbrandofficial',
    
    # Offensive and inappropriate terms (keep a separate list if possible)
    'badword1', 'badword2',  # Add specific terms to avoid in your app

    # Social media or internet handles
    'facebook', 'twitter', 'instagram', 'linkedin', 'snapchat', 'youtube', 'reddit',

    # Reserved terms for specific purposes (if applicable)
    'mail', 'email', 'account', 'profile', 'settings', 'config', 'privacy', 
    'login', 'logout', 'signin', 'signup', 'register'
    
    # Reserved terms for this project
    'inbox',
]