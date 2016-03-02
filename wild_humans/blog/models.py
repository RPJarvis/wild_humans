from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, max_length=140)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])