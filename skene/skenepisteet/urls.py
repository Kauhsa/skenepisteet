from django.conf.urls.defaults import *
from skene.skenepisteet.views import index, info_popup, history_popup

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^popup/info/(?P<scener_id>\d+)$', info_popup),
    url(r'^popup/history/(?P<scener_id>\d+)$', history_popup),
)