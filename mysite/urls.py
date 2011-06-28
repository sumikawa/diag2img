from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^json/', include('mysite.nw.urls')),
    (r'^nw/', include('mysite.nw.urls')),

    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/usr/local/src/diag2img/mysite/js'}),
)
