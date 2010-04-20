from django.conf.urls.defaults import *

urlpatterns = patterns('gallery.views',
    url(r'^$', "index", name="gallery_index"),
)

