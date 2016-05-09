from django.conf.urls import patterns, url

urlpatterns = patterns('ciec_portail.views',
    url(r'^$','ciec_home',name="ciec_home"),
    url(r'^candidature_ciec$','candidature_ciec',name="candidature_ciec"),
    url(r'^candidature_instance$','candidature_instance',name="candidature_instance"),

)
