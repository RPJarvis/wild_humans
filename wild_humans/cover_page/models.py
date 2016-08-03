from django.db import models

# Create your models here.
class CoverImage():
    image = models.ImageField()
    alt_text = models.CharField(max_length=40)
    caption = models.CharField(max_length=140)