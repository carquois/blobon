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
    url(r'^$', 'punns.views.index'),
    url(r'^new/$', 'punns.views.new'),
    url(r'^moderate/$', 'punns.views.moderate'),
    url(r'^news/$', 'news.views.all'),
    url(r'^earnings/$', 'earnings.views.index'),
    url(r'^create/$', 'punns.views.create'),
    url(r'^create-from-rss/$', 'punns.views.create_from_rss'),
    url(r'^createcat/$', 'punns.views.createcat'),
    url(r'^r/(?P<slug>.*)/$', 'punns.views.cat'),
    url(r'^delete/(?P<id>.*)/$', 'comments.views.delete'),
    url(r'^punn-delete/(?P<id>.*)/$', 'punns.views.delete'),
    url(r'^hot/(?P<id>.*)/$', 'punns.views.hot'),
    url(r'^up/(?P<id>.*)/$', 'votes.views.up'),
    url(r'^down/(?P<id>.*)/$', 'votes.views.down'),
    url(r'^comment-up/(?P<id>.*)/$', 'votes.views.commentup'),
    url(r'^comment-down/(?P<id>.*)/$', 'votes.views.commentdown'),
    url(r'^reblog/(?P<id>.*)/$', 'punns.views.reblog'),
    url(r'^favorite/(?P<id>.*)/$', 'punns.views.favorite'),
    url(r'^p/(?P<shorturl>.*)/$', 'punns.views.single'),
    url(r'^c/(?P<shorturl>.)/$', 'punns.views.comment'),
    url(r'^s/$', 'punns.views.search'),
    url(r'^f/(?P<username>.*)/$', UserFeed()),
    url(r'^signup/$', 'accounts.views.signup'),
    url(r'^signup-step2/$', 'accounts.views.social_signup_step2'),
    url(r'^new-association/$', 'accounts.views.new_association'),
    url(r'^register/$', 'accounts.views.register'),
    url(r'^discover/$', 'accounts.views.discover'),
    url(r'^random/$', 'punns.views.random'),
#    url(r'^top/today$', 'punns.views.today'),
#    url(r'^top/week$', 'punns.views.week'),
#    url(r'^top/month$', 'punns.views.month'),
#    url(r'^top/all$', 'punns.views.top'),
    url(r'^submit/$', 'punns.views.submit'),
    url(r'^draft/$', 'punns.views.draft'),
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
