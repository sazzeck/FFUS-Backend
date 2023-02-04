import typing as t
from rest_framework import serializers

from .models import ContactModel


class ContactSerializer(serializers.ModelSerializer):
    firstname: serializers.CharField = serializers.CharField(
        max_length=64, min_length=3, required=True
    )

    class Meta:
        model: t.Type[ContactModel] = ContactModel
        fields: list[str] = ["firstname", "phone_number"]
