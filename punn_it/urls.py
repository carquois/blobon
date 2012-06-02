from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'punns.views.index'),
    url(r'^p/(?P<shorturl>.)/$', 'punns.views.single'),
    url(r'^s/(?P<shorturl>.)/$', 'punns.views.tag'),
    url(r'^c/(?P<shorturl>.)/$', 'punns.views.comment'),
    url(r'^signup/$', 'punns.views.signup'),
    url(r'^submit/$', 'punns.views.submit'),
    url(r'^login/$',  login),
    url(r'^logout/$', logout),
    url(r'^settings/profile/$', 'punns.views.edit_profile'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<user>[^/]+)/$', 'punns.views.profile_page'), 
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT,
        }),
   )

urlpatterns += staticfiles_urlpatterns()

