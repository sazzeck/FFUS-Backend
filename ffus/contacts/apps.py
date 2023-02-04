import typing as t

from django.apps import AppConfig


class ContactsConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: t.Literal["contacts"] = "contacts"
