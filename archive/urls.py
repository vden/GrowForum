from django.conf.urls.defaults import *

urlpatterns = patterns('archive.views',
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', "index"),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', "index"),
    url(r'^(?P<year>\d+)/$', "index"),
    url(r'^$', "index", name="archive_index"),
)

