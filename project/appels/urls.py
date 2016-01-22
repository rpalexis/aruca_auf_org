# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('appels.views',
    url(r'appels-offre/$', 'appel_offre'),
    url(r'^appels-offre/(?P<slug>[-\w]+)/$', 'appel_offre_detail'),
)