"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import environ
from pathlib import Path
import pkg_resources


root = environ.Path(__file__) - 2  # get root of the project
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(root())

# initialize env with environment variable
# it can contains DEBUG (in production env it shall)
# so we could explore how to load file only on local execution
env = environ.Env()

env_path = BASE_DIR / ".env"
if env_path.is_file():
    environ.Env.read_env(str(env_path))  # reading .env file


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_APPS = [
    "crispy_forms",
]

PROJECT_APPS = [
    "users.apps.UsersConfig",
    "blog.apps.BlogConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
        ],
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
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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


# indicate the new User model to Django
AUTH_USER_MODEL = "users.User"


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = str(BASE_DIR / "staticroot")

STATICFILES_DIRS = [
    BASE_DIR / "static",
    # BASE_DIR / "htmlcov",
]

# same goes for media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# specify to django we use only S3 to store files
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# credentials
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")

# bucket name and region
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME")
AWS_DEFAULT_ACL = 'public-read'

# append a prefix to all uploaded file (useful to not mix local, staging...)
AWS_LOCATION = env.str("AWS_LOCATION")
# avoid overriding a file if same key is provided
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False

# Crispy configuration
# https://django-crispy-forms.readthedocs.io/en/latest/index.html
# set default rendering
CRISPY_TEMPLATE_PACK = "bootstrap4"


# django-debug-toolbar configuration

# activate only if debug is True
# and only if package is available
if DEBUG:
    try:
        # only if debug_toolbar is available, else it will fire exception
        # useful to turn debug mode on staging without installing dev dependencies
        import debug_toolbar  # noqa: F401

        INSTALLED_APPS += ["debug_toolbar"]
        MIDDLEWARE += [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]

        # bypass check of internal IPs
        def show_toolbar(request):
            return True

        DEBUG_TOOLBAR_CONFIG = {
            "SHOW_TOOLBAR_CALLBACK": show_toolbar,
        }

    except ImportError:
        pass

    if "django-extensions" in {pkg.key for pkg in pkg_resources.working_set}:
        INSTALLED_APPS += [
            "django_extensions",
        ]
