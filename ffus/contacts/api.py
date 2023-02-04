import typing as t

from rest_framework.viewsets import mixins, GenericViewSet
from django.db import models

from .serializers import ContactSerializer
from .models import ContactModel


class ContactsViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    serializer_class: t.Type[ContactSerializer] = ContactSerializer
    queryset: models.Manager = ContactModel.objects.all()
