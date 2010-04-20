from django.conf.urls.defaults import *

urlpatterns = patterns('files.views',
    url(r'^$', "index", name='files_index'),
)

