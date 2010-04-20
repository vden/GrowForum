from django.conf.urls.defaults import *

urlpatterns = patterns('chat.views',
    url(r'^$', "index", name="chat_index"),
)

