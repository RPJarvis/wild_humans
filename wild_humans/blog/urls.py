"""URLs for the social_media_links app."""
from django.conf.urls import patterns, url
from . import views
# from . import views


# urlpatterns = patterns(
#     '',
#     url(r'^$',
#         views.YourView.as_view(),
#         name='social_media_links_default'),
# )

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post' )
)
