from django.contrib import admin
from . import models
# Register your models here.
class EventCalendarAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'venue', 'passed']

admin.site.register(models.Event, EventCalendarAdmin)