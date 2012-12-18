from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from punns.views import UserFeed
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^settings/profile/$', 'accounts.views.edit_profile'),
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
    url(r'^$', 'punns.views.index', {'draft': False}),
    url(r'^p/(?P<shorturl>.*)/$', 'punns.views.single'),
    url(r'^c/(?P<shorturl>.)/$', 'punns.views.comment'),
    url(r'^s/$', 'punns.views.search'),
    url(r'^f/(?P<username>.*)/$', UserFeed()),
    url(r'^signup/$', 'accounts.views.signup'),
    url(r'^random/$', 'punns.views.random'),
    url(r'^submit/$', 'punns.views.submit'),
    url(r'^draft/$', 'punns.views.index', {'draft': True}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/$', 'punns.views.home'),
    url(r'^done/$', 'punns.views.done'),
    url(r'^(?P<user>[^/]+)/$', 'punns.views.profile_page'), 
    url(r'', include('social_auth.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^i/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + urlpatterns

    #static hosting for dev server
    urlpatterns += staticfiles_urlpatterns()
