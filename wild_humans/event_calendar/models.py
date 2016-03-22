from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField()
    venue = models.CharField(max_length=140)
    description = models.CharField(max_length=240)

    #method to check if event has passed
    class Meta():
        ordering = ['-date']

    def __unicode__(self):
        return u'%s' % self.title