# -*- coding: utf-8 -*-

# Django settings for punn_it project.
import os

try:
    import social_auth
except ImportError:
    import sys
    sys.path.insert(0, "..")

DEBUG = False 
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = False 

ADMINS = (
     ('Vincent Gauthier', 'vincegothier@gmail.com')
    # ('Gabriel Dancause', 'errors@blobon.com'),
)

ACCOUNT_ACTIVATION_DAYS = 21

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

MAIN_SITE_DESCRIPTION = "Cliquez sur la vignette pour afficher l'image en pleine grandeur"
MAIN_SITE_DOMAIN = "checkdonc.ca"

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 9621440

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'punns',     # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'a74108520Q',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 8 

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = 'http://punnitimages.s3-website-us-east-1.amazonaws.com/'
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_DIR), 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'assets'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'dajaxice.finders.DajaxiceFinder',
    'compressor.finders.CompressorFinder',
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAJZRKVK6EZ5KCWBAA'
AWS_SECRET_ACCESS_KEY = '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'
BUCKET_UPLOADS = 'i.checkdonc.ca'
BUCKET_UPLOADS_URL = '//i.checkdonc.ca/'
AWS_STORAGE_BUCKET_NAME = 'punnitimages'
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
AWS_S3_CUSTOM_DOMAIN = "i.checkdonc.ca"

# For your production site, link to the S3 uploads bucket.
# This setting is optional for development.
PRODUCTION = False

THUMBNAIL_BACKEND = 'punns.thumbnails.PunnItThumbnailBackend'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

# Close the session when user closes the browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@ydy$0c!6jgz68m1l^y9hz#)_hq(5v0@kn13%14q+dw=oa1c5%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'accounts.middleware.AccountMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'blobon.urls'

LOGOUT_URL = '/logout'
LOGIN_URL = 'accounts/login'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

#TINYMCE
TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js' 
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True



#SOCIAL AUTH 
FACEBOOK_APP_ID = '378058345602851'
FACEBOOK_API_SECRET = '1f0ab1daa0b5dfd0d2c21b5c05d82607'
FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_birthday', 'user_likes', ]

TWITTER_CONSUMER_KEY         = 'QIgYelwN2RHao8Pbs57otQ'
TWITTER_CONSUMER_SECRET      = 'nw5al39gQhhH1QxTEXKfy5s32yjNIB9OK7S42V5ZPU'

GOOGLE_OAUTH2_CLIENT_ID = '416854741815.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'zQ8NlUiLFUdAEjjrhik7PSQt'

SOCIAL_AUTH_RAISE_EXCEPTIONS = DEBUG
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
#TODO CUSTOMIZE THE URLs 
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/signup-step2/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/accout-disconnected-redirect-url/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/signup/'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME      = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME     = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_BY_MAIL     = False
LOGIN_ERROR_URL                   = '/login/error/'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SOCIAL_AUTH_EXPIRATION = 'expires'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    #twitter, facebook and google all validate emails, so it's ok to associate_by_email
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'accounts.pipeline.load_facebook_extra_data',
)


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = "587"
EMAIL_HOST_USER = 'blobon@blobon.com'
EMAIL_HOST_PASSWORD = 'a74108520Q'
EMAIL_USE_TLS = True


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.markup', 
    'south',
    'dajaxice',
    'dajax',
    'social_auth',
    'sorl.thumbnail',
    'punns',
    'earnings',
    'comments',
    'accounts',
    'blogs',
    'images',
    'votes',
    #'posts',
    #'pages',
    'news',
    'notifications',
    'registration',
    'gunicorn',
    'compressor',
    'dbdump',
    'django_extensions',
    'raven.contrib.django.raven_compat',
    's3sync',
    'storages',
    'tinymce',
    'books',
    'mathfilters',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    #SOCIAL_AUTH 
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_login_redirect',
    #Project context processors
    "punns.context_processors.login_url_with_redirect",
)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

RAVEN_CONFIG = {
    'dsn': 'http://070d2c289845436992740242e43df5e2:f4b0d09136f546f3ada2d6cf90dd6334@sentry.checkdonc.ca/2',
}




try:
    from local_settings import *
except:
    pass


