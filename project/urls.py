# -*- encoding: utf-8 -*

from django.conf.urls.defaults import patterns, include, \
        handler500, handler404, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from filebrowser.sites import site
from feeds import DerniersAjouts

admin.autodiscover()

handler404
handler500 # Pyflakes

urlpatterns = patterns(
    '',
    # admin
    url(r'^tinymce/', include('tinymce.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^flux-rss/$', DerniersAjouts()),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('project.annuaire.urls')),
    (r'^', include('project.appels.urls')),
    (r'^', include('project.contact.urls')),
    (r'^', include('project.photos.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

#search
urlpatterns += patterns('views',
    (r'^recherche/$', 'search'),
    (r'^a-propos/$', TemplateView.as_view(template_name='propos.html')),
    (r'^aide/$',  TemplateView.as_view(template_name='aide.html')),
    (r'^liens-utiles/$',  TemplateView.as_view(template_name='liens.html')),
)

# django-cms
urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
        'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT, }),
        )
