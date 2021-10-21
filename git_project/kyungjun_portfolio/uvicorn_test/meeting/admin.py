from django.contrib import admin
from .models import Room, Meeting


# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    pass
