from django.contrib import admin

# Register your models here.

from .models import Pet, Message

admin.site.register(Pet)
admin.site.register(Message)