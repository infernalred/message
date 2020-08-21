from django.contrib import admin

from .models import Postman


@admin.register(Postman)
class PostmanAdmin(admin.ModelAdmin):
    list_display = ("email", "text", "sent")


