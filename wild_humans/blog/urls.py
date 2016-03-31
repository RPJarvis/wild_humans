
from django.conf.urls import patterns, url
from . import views





urlpatterns = patterns('',
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post' )
)

