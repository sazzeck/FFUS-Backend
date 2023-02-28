from rest_framework.routers import SimpleRouter
from django.urls import URLPattern
from .api import FeedbackViewSet


contacts: SimpleRouter = SimpleRouter()

contacts.register("feedback", FeedbackViewSet)

urlpatterns: list[URLPattern] = contacts.urls
