import os
from pathlib import Path
from datetime import timedelta
from django.conf import settings
from dotenv import load_dotenv
from os import getenv

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = getenv("SECRET_KEY")
DEBUG = getenv("DEBUG") == '1'
ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',
    'solo',
    'tinymce',
    'imagekit',
    'django_filters',
    'cadp_about',
    'cadp_content',
    'cadp_report',
    'cadp_media',
    'cadp_contact',
    'cadp_polls',
    'users',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda request: True,
# }

ROOT_URLCONF = 'config.urls'

# TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ ],
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

WSGI_APPLICATION = 'config.wsgi.application'


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


AUTH_USER_MODEL = 'users.CustomUser'


# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',

# )

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('uz', 'Uzbek'),
)

# LOCALE_PATHS = [
#     BASE_DIR / 'locale',
# ]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

# LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

JAZZMIN_SETTINGS = {
    "site_title": "CADP Admin Panel",
    "site_header": "CADP Admin",
    "welcome_sign": "CADP Admin Panel",
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.alerts.AlertsPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

# Celery Configuration Options
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'


# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = "a.sarvar2005@gmail.com"
EMAIL_HOST_PASSWORD = "reeq ttuj kjnf khpx"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'a.sarvar2005@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "100%",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image imagetools charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | blockquote | image | fullscreen | fontselect fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
               "a11ycheck ltr rtl | showcomments addcomment code",
    "imagetools_toolbar": "rotateleft rotateright | flipv fliph | editimage imageoptions",
    "imagetools_cors_hosts": ['mydomain.com', 'otherdomain.com'],
    "imagetools_proxy": 'proxy.php',
    'image_advtab': True,
    "custom_undo_redo_levels": 10,
    'images_upload_url': '/api/upload_image/',  # add to plugin: image imagetools
    'relative_urls': False,
    'remove_script_host': False,
    'convert_urls': True,
    'fontsize_formats': "8px 9px 10px 11px 12px 14px 16px 18px 24px 30px 36px 48px 60px 72px 96px"
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

SWAGGER_SETTINGS = {
    'DEFAULT_FIELD_INSPECTORS': [
        'drf_yasg.inspectors.CamelCaseJSONFilter',
        'drf_yasg.inspectors.InlineSerializerInspector',
        'drf_yasg.inspectors.RelatedFieldInspector',
        'drf_yasg.inspectors.ChoiceFieldInspector',
        'drf_yasg.inspectors.FileFieldInspector',
        'drf_yasg.inspectors.DictFieldInspector',
        'drf_yasg.inspectors.SimpleFieldInspector',
        'drf_yasg.inspectors.StringDefaultFieldInspector',
    ],}