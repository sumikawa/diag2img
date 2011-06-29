from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os

urlpatterns = patterns('',
    (r'^json/', include('mysite.nw.urls')),
    (r'^nw/', include('mysite.nw.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^js/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.STATIC_ROOT, 'js')}),
    )
