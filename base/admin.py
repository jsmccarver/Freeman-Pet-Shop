from django.contrib import admin

# Register your models here.

from .models import Pet, Message, Room, Topic

admin.site.register(Pet)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Topic)
