from django.contrib import admin
from . import models
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'publish_date' ]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Blog, BlogAdmin)

