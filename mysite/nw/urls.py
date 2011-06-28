from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mysite.nw.views',
    (r'^(?P<diag>[\d\w\/+=]+).png', 'show'),
    (r'^edit/(?P<diag>[\d\w\/+=]+)$', 'edit'),
    (r'^json/$', 'json'),
)
