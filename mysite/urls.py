from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^json/', include('mysite.img.urls')),
    (r'^img/', include('mysite.img.urls')),

    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/usr/local/src/diag2img/mysite/js'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
