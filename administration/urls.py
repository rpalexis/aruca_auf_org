from django.conf.urls import patterns, url

urlpatterns = patterns('administration.views',
    url(r'^$','adm_home',name="adm_home"),
    url(r'^liste_instances/$','instances',name="instances"),
    url(r'^liste_candidats/$','candidats',name="candidats"),
    url(r'^csv_exporting/$','csv_exporting',name="csv_exporting"),
    url(r'^csv_exporting_2/$','csv_exporting_2',name="csv_exporting_2"),
)
