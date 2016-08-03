from django.contrib import admin
from . import models
# Register your models here.
class CoverImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'alt_text', 'caption']

admin.site.register(models.CoverImage, CoverImageAdmin)