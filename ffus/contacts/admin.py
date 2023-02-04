from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "phone_number", "date_created")
    list_filter = ("date_created", "id")
    search_fields = ("phone_number",)
