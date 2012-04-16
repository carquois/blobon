from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'punn.views.index'),
    url(r'^p/(?P<shorturl>.)/$', 'punn.views.detail'),
    url(r'^p/create/$', 'punn.views.create'),

    #TODO http://www.djangobook.com/en/beta/chapter12/
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<user>[^/]+)/$', 'punn.views.profile_page'), 
)

