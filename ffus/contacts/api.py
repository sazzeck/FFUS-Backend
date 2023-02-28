import typing as t

from rest_framework.viewsets import mixins, GenericViewSet
from django.db import models

from .serializers import FeedbackSerializer
from .models import FeedbackModel


class FeedbackViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class: t.Type[FeedbackSerializer] = FeedbackSerializer
    queryset: models.Manager = FeedbackModel.objects.all()
