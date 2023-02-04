import typing as t

from django.db import models
from phonenumber_field import modelfields
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    firstname: models.CharField = models.CharField(
        verbose_name=_("Ім'я"),
        max_length=64,
        blank=False,
        null=False,
    )
    phone_number: modelfields.PhoneNumberField = modelfields.PhoneNumberField(
        verbose_name=_("Номер телефону"),
        max_length=13,
        blank=False,
        null=False,
        unique=True,
    )
    date_created: models.DateTimeField = models.DateTimeField(
        verbose_name=_("Дата створення"),
        auto_now_add=True,
    )

    class Meta:
        db_table: t.Literal["contacts"] = "contacts"
        verbose_name: str = _("Контакт")
        verbose_name_plural: str = _("Контакти")
        ordering: list[str] = ["id", "date_created"]

    def __str__(self) -> str:
        return f"{self.firstname}".capitalize()
