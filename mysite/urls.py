from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^json/', include('nw.urls')),
    (r'^nw/', include('nw.urls')),

    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/dotcloud/current/js'}),
)
