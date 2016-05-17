from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=240)
    url = models.URLField()
    embed_code = models.TextField(max_length=2048)