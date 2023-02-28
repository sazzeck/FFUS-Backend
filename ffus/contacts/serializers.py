import typing as t
from rest_framework import serializers

from .models import FeedbackModel


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model: t.Type[FeedbackModel] = FeedbackModel
        fields: list[str] = ["id", "firstname", "phone_number"]
