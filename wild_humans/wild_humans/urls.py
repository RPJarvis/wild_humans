from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('wild_humans_main.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^calendar/', include('event_calendar.urls')),
    url(r'^videos/', include('videos.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
