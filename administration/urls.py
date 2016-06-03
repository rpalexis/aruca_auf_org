from django.conf.urls import patterns, url

urlpatterns = patterns('administration.views',
    url(r'^$','adm_home',name="adm_home"),
)
