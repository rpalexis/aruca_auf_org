# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('photos.views',
    url(r'album/$', 'album'),
    url(r'^album/(?P<id>[-\w]+)/$', 'album_detail'),
)