# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from filebrowser.sites import site
from feeds import DerniersAjouts

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^$','views.acc'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^flux-rss/$', DerniersAjouts()),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    #Apps urls
    url(r'^annuaire/', include('annuaire.urls')),
    url(r'^appels/', include('appels.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^photos/', include('photos.urls')),
    #Apps urls
    #search
    url(r'^recherche/$', 'views.search'),
    url(r'^a-propos/$', 'views.propos'),
    url(r'^aide/$', 'views.help'),
    url(r'^liens-utiles/$', 'views.useful'),
    #search
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^t/', include('cms.urls')),

)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
