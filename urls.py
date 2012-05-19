from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'punn.views.index'),
    url(r'^p/(?P<shorturl>.)/$', 'punn.views.single'),
    url(r'^s/(?P<shorturl>.)/$', 'punn.views.tag'),
    url(r'^c/(?P<shorturl>.)/$', 'punn.views.comment'),
    url(r'^signup/$', 'punn.views.signup'),
    url(r'^submit/$', 'punn.views.submit'),
    url(r'^login/$',  login),
    url(r'^logout/$', logout),
    url(r'^settings/profile/$', 'punn.views.edit_profile'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<user>[^/]+)/$', 'punn.views.profile_page'), 
)

