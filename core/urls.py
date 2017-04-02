from django.conf.urls import patterns,url
from.views import *

urlpatterns = patterns('',
                       url(r'^$',home,name='home'),
                       url(r'^artists/$',artist_lists,name='artists'),
                       url(r'^playlist/$',playlist,name='playlist'),
)