import os

from django.core.asgi import get_asgi_application
from django.core.handlers.asgi import ASGIHandler

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "app.settings.production",
)


application: ASGIHandler = get_asgi_application()
