# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('contact.views',
    url(r'contact/$', 'contact'),
)