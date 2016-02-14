from django.contrib import admin
from . import models
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'publish_date' ]

admin.site.register(models.Blog, BlogAdmin)

