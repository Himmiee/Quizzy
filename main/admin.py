from django.contrib import admin

from . import models

# Register your models here.

class AdminSettings(admin.ModelAdmin):
    list_display = ("course","question", "created", "updated")

admin.site.register(models.Detail, AdminSettings)
admin.site.register(models.Course)
admin.site.register(models.Option)