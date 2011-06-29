from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('facebook.facebook_connect.views',
    (r'^$', 'connect'),
    (r'^done/$', 'done'),
)