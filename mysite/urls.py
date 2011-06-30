import os
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    (r'^json/', include(settings.SITE_ROOT + 'nw.urls')),
    (r'^nw/', include(settings.SITE_ROOT + 'nw.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^js/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.STATIC_ROOT, 'js'), }),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.STATIC_ROOT, 'css'), }),
    )
