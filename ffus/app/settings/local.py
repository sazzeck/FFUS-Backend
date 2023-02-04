import typing as t

from .settings import *  # noqa
from .settings import BASE_DIR

DEBUG: bool = True

DATABASES: dict[str, t.Union[str, int]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": f"{BASE_DIR}/database/db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", # noqa
    },
]
