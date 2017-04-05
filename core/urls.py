from django.conf.urls import patterns,url
from.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^$',home,name='home'),
                       url(r'^artists/$',artist_lists,name='artists'),
                       url(r'^artist_detail/(?P<pk>\d+)/$',artist_detail,name='artist_detail'),
                       url(r'^playlist/$',playlist,name='playlist'),
                       url(r'^whats_new/$',whats_new,name='whats_new'),
                       url(r'^upload/$',upload,name='upload'),
) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)