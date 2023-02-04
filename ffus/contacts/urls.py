from rest_framework.routers import SimpleRouter
from django.urls import URLPattern
from .api import ContactsViewSet


contacts: SimpleRouter = SimpleRouter()

contacts.register(r"contacts", ContactsViewSet)

urlpatterns: list[URLPattern] = contacts.urls
