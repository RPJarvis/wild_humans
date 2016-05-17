from django.contrib import admin
from . import models
# Register your models here.
class VideosAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'embed_code']

admin.site.register(models.Video, VideosAdmin)