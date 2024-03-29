from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.conf.urls.static import static
from django.contrib import admin
from skene import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('skene.skenepisteet.urls')),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
