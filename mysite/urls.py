import os
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    ('^$', redirect_to, {'url': '/block/'}),
    (r'^nw/', include(settings.SITE_ROOT + 'nw.urls')),
    (r'^block/', include(settings.SITE_ROOT + 'block.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^js/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.STATIC_ROOT, 'js'), }),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.STATIC_ROOT, 'css'), }),
    )
