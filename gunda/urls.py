from django.conf.urls import patterns, include, url
from django.contrib import admin
import core

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gunda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(core.urls,namespace='core')),
)
