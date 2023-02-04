# import typing as t
from pathlib import Path

from ffus.utils import Config

SECRET_KEY: str = Config.SECRET_KEY

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

ALLOWED_HOSTS: list[str] = Config.HOSTS


CREATED_APPS: list[str] = [
    "contacts",
]

INSTALLED_APPS: list[str] = [
    "rest_framework",
    "phonenumber_field",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
] + CREATED_APPS

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "app.urls"

# TEMPLATES: list[dict[str, t.Any]] = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [Path(BASE_DIR, "templates")],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]


CORS_ALLOWED_ORIGINS: list[str] = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CORS_ALLOW_METHODS: list[str] = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


WSGI_APPLICATION: str = "app.wsgi.application"

LANGUAGE_CODE: str = Config.LANGUAGE

TIME_ZONE: str = Config.TIME_ZONE

DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

USE_I18N: bool = True

USE_L10N: bool = True

USE_TZ: bool = True

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"

PHONENUMBER_DEFAULT_REGION: str = Config.PHONENUMBER_REGION
