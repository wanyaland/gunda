from django.conf.urls import patterns,url

urlpatterns = patterns('',
                       url(r'^login/$','accounts.views.login_user',name='login'),
                       url(r'^logout/$','accounts.views.logout_user',name='logout'),
                       url(r'^sign_up/$','accounts.views.sign_up',name='sign_up')
                       )

