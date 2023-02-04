from django.contrib import admin
from django.urls import URLResolver, include, path

from ffus.utils import Config

urlpatterns: list[URLResolver] = [
    path(Config.ADMIN_PANEL_URL, admin.site.urls),
    path(Config.API_URL, include("contacts.urls")),
]
