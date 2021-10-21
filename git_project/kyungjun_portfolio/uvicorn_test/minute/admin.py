from django.contrib import admin
from .models import Minute

# Register your models here.


@admin.register(Minute)
class MinuteAdmin(admin.ModelAdmin):
    pass
