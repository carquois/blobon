from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^settings/profile/$', 'punns.views.edit_profile'),
    #TODO hook the password change page
    url(r'^settings/password/$', 'django.contrib.auth.views.password_change',
                          {'post_change_redirect': '/settings/password/password_reset_confirmation/'}),
    url(r'^settings/password/password_reset_confirmation/$', 'django.contrib.auth.views.password_change_done'),
    url(r'', include('social_auth.urls')),
    url(r'^$', 'punns.views.index'),
    url(r'^p/(?P<shorturl>.)/$', 'punns.views.single'),
    url(r'^s/(?P<shorturl>.)/$', 'punns.views.tag'),
    url(r'^c/(?P<shorturl>.)/$', 'punns.views.comment'),
    url(r'^top/$', 'punns.views.top'),
    url(r'^top/day$', 'punns.views.top_day'),
    url(r'^signup/$', 'punns.views.signup'),
    url(r'^submit/$', 'punns.views.submit'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<user>[^/]+)/$', 'punns.views.profile_page'), 
)

