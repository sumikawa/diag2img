from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns(settings.SITE_ROOT + 'nw.views',
    (r'^(?P<diag>[\d\w\/+=]*).png', 'show'),
    (r'^edit/(?P<diag>[\d\w\/+=]*)$', 'edit'),
    (r'^json/$', 'json'),
)
