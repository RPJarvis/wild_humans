from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^listen', views.listen, name='listen'),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^$', views.index, name='index'), #this should be last

]