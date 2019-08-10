## These settings will overrid any default settings set in the standard Django app and the `hacko_settings.py` included in docker container

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG").lower() == "true"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "corsheaders",
    "django_filters",
    "rest_framework",
    "rest_framework_gis",
    "rest_framework_swagger",
    "health_check",  # required
    "health_check.db",  # stock Django health checkers
    "health_check.storage",
    "health_check.contrib.psutil",  # disk and memory utilization; requires psutil
    "toad",
]

HEALTH_CHECK = {"DISK_USAGE_MAX": 90, "MEMORY_MIN": 100}  # percent  # in MB

DATABASE_ROUTERS = ["backend.router.ModelDatabaseRouter"]

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
        "OPTIONS": {"options": "-c search_path=trimet_gis,public"},
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/transportation2019/static/"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}
