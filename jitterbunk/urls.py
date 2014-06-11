from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # main feed, displays all bunks
                       url(r'^bunks/$', 'jitterbunk_app.views.main_feed'),
                       # user feed, displays bunks either to or from user
                       url(r'^bunks/(?P<user_name>\w+)',
                           'jitterbunk_app.views.personal_feed'),
                       # handles adding bunks
                       url(r'^bunked/$', 'jitterbunk_app.views.bunked'))
