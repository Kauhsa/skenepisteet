from django.conf.urls.defaults import *
from skene.skenepisteet.views import index, info_popup, login_popup, logout_view

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^popup/info/(?P<scener_id>\d+)$', info_popup),
)