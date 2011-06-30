import os
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    ('^$', redirect_to, {'url': '/block/'}),
    (r'^act/', include(settings.SITE_ROOT + 'act.urls')),
    (r'^block/', include(settings.SITE_ROOT + 'block.urls')),
    (r'^nw/', include(settings.SITE_ROOT + 'nw.urls')),
    (r'^seq/', include(settings.SITE_ROOT + 'seq.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^js/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.STATIC_ROOT, 'js'), }),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.STATIC_ROOT, 'css'), }),
    )
