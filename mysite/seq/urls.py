from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns(settings.SITE_ROOT + 'seq.views',
    (r'^(?P<diag>[\d\w\/+=]*).png', 'show'),
    (r'^(?P<diag>[\d\w\/+=]*)$', 'edit'),
)
