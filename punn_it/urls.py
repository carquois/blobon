from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^settings/profile/$', 'punns.views.edit_profile'),
    url(r'^settings/password/$', 'django.contrib.auth.views.password_change',
                          {'post_change_redirect': '/settings/password/password_reset_confirmation/'}),
    url(r'^settings/password/password_reset_confirmation/$', 'django.contrib.auth.views.password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', 
                          {'template_name': 'registration/password_reset_form.html',
                           'email_template_name': 'registration/password_reset_email.html'}),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', 
			  {'template_name': 'registration/password_reset_done.html'}),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
                          {'template_name': 'registration/password_reset_confirm.html'}),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', 
			  {'template_name': 'registration/password_reset_complete.html'}),
    url(r'^$', 'punns.views.index'),
    url(r'^p/(?P<shorturl>.*)/$', 'punns.views.single'),
    url(r'^d/(?P<shorturl>.*)/$', 'punns.views.singletest'),
    url(r'^c/(?P<shorturl>.)/$', 'punns.views.comment'),
    url(r'^signup/$', 'punns.views.register'),
    url(r'^submit/$', 'punns.views.submit'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<user>[^/]+)/$', 'punns.views.profile_page'), 
)

