from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^punn_it/', include('punn_it.foo.urls')),
    url(r'^$', 'punn.views.index'),
    url(r'^punn/create/$', 'punn.views.create'),
    url(r'^punn/(?P<shorturl>.)/$', 'punn.views.detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

