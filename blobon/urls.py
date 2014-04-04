from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin
from punns.views import UserFeed
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from accounts.forms import Blobon_loginForm
dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^accounts/login/$', 'accounts.views.custom_login'),
    url(r'^accounts/blobon_login/$', 'accounts.views.blobon_login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^login/$', 'django.contrib.auth.views.login', 
                          {'template_name': 'login.html', 'authentication_form':Blobon_loginForm}),
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
    url(r'^$', 'blogs.views.index'),
    url(r'^pics/$', 'blogs.views.pics'),
    #url(r'^videos/$', 'blogs.views.videos'),
    url(r'^new/$', 'punns.views.new'),
    url(r'^moderate/$', 'punns.views.moderate'),
    url(r'^twitter/$', 'accounts.views.twitter'),
    url(r'^twitter-success/$', 'accounts.views.twitter_success'),
    url(r'^news/$', 'news.views.all'),
    url(r'^earnings/$', 'earnings.views.index'),
    url(r'^createblog/$', 'blogs.views.createblog'),
    url(r'^newpost/(?P<slug>.*)/$', 'blogs.views.newpost'),
    url(r'^subscribe/(?P<slug>.*)/$', 'blogs.views.subscribe_to_infoletter'),
    url(r'^savedraft/(?P<slug>.*)/$', 'blogs.views.savedraft'),
    url(r'^newcategory/(?P<slug>.*)/$', 'blogs.views.newcategory'),
    url(r'^newrss/(?P<slug>.*)/$', 'blogs.views.newrss'),
    url(r'^newemail/(?P<slug>.*)/$', 'blogs.views.create_info_email'),
    url(r'^page/(?P<slug>.*)/$', 'blogs.views.page'),
    url(r'^createpage/(?P<slug>.*)/$', 'blogs.views.createpage'),
    url(r'^dashboard/$', 'blogs.views.dashboard'),
    url(r'^dashboard/(?P<slug>.*)/$', 'blogs.views.administrateblog'),
    url(r'^administrateposts/(?P<slug>.*)/$', 'blogs.views.administrateposts'),
    url(r'^queue/(?P<slug>.*)/$', 'blogs.views.queue'),
    url(r'^published/(?P<slug>.*)/$', 'blogs.views.published'),
    url(r'^translation/(?P<slug>.*)/$', 'blogs.views.translation'),
    url(r'^quicktranslation/(?P<slug>.*)/$', 'blogs.views.quicktranslation'),
    url(r'^translatepost/(?P<id>.*)/$', 'blogs.views.translatepost'),
    url(r'^billing/(?P<id>.*)/$', 'books.views.invoice'),
    url(r'^administratepages/(?P<slug>.*)/$', 'blogs.views.administratepages'),
    url(r'^administratecomments/(?P<slug>.*)/$', 'blogs.views.administratecomments'),
    url(r'^administratecategories/(?P<slug>.*)/$', 'blogs.views.administratecategories'),
    url(r'^rss_auto/(?P<slug>.*)/$', 'blogs.views.rss_auto_post'),
    url(r'^administrateemails/(?P<slug>.*)/$', 'blogs.views.administrateemails'),
    url(r'^administratetags/(?P<slug>.*)/$', 'blogs.views.administratetags'),
    url(r'^administratesettings/(?P<slug>.*)/$', 'blogs.views.administratesettings'),
    url(r'^editpost/(?P<id>.*)/$', 'blogs.views.editpost'),
    url(r'^editpage/(?P<id>.*)/$', 'blogs.views.editpage'),
    url(r'^fastedit/(?P<slug>.*)/$', 'blogs.views.fastedit'),
    url(r'^fasteditpost/(?P<id>.*)/$', 'blogs.views.fasteditpost'),    
    url(r'^editemail/(?P<id>.*)/$', 'blogs.views.editemail'),
    url(r'^previewemail/(?P<id>.*)/$', 'blogs.views.view_info_letter'),
    url(r'^editcategory/(?P<id>.*)/$', 'blogs.views.editcategory'),
    url(r'^approve/(?P<id>.*)/$', 'blogs.views.approvecomment'),
    url(r'^create/$', 'punns.views.create'),
    url(r'^contact/$', 'blogs.views.contact'),
    url(r'^password/(?P<slug>.*)/$', 'blogs.views.password'),
    url(r'^passwordsingle/(?P<id>.*)/$', 'blogs.views.passwordsingle'),
    url(r'^newcomment/(?P<id>.*)/$', 'blogs.views.newcomment'),
    url(r'^signalcomment/(?P<id>.*)/$', 'blogs.views.signalcomment'),
    url(r'^entreprise/$', 'blogs.views.entreprise'),
    url(r'^send/(?P<id>.*)/$', 'blogs.views.send_email_now'),
    url(r'^create-from-rss/$', 'punns.views.create_from_rss'),
    url(r'^createcat/$', 'punns.views.createcat'),
    url(r'^createalbum/$', 'punns.views.createalbum'),
    url(r'^universal/$', 'punns.views.universal'),
    url(r'^c/(?P<slug>.*)/$', 'punns.views.cat'),
    url(r'^cat/(?P<slug>.*)/$', 'blogs.views.category'),
    url(r'^delete/(?P<id>.*)/$', 'comments.views.delete'),
    url(r'^punn-delete/(?P<id>.*)/$', 'punns.views.delete'),
    url(r'^deletepost/(?P<id>.*)/$', 'blogs.views.deletepost'),
    url(r'^deletepost_trans/(?P<id>.*)/$', 'blogs.views.deletepost_trans'),
    url(r'^deletepage/(?P<id>.*)/$', 'blogs.views.deletepage'),
    url(r'^deletecategory/(?P<id>.*)/$', 'blogs.views.deletecategory'),
    url(r'^deleterss/(?P<id>.*)/$', 'blogs.views.deleterss'),
    url(r'^publishnow/(?P<id>.*)/$', 'blogs.views.publish_now'),
    url(r'^publishpagenow/(?P<id>.*)/$', 'blogs.views.publish_page_now'),
    url(r'^deletecomment/(?P<id>.*)/$', 'blogs.views.deletecomment'),
    url(r'^deletecommentsingle/(?P<id>.*)/$', 'blogs.views.deletecomment_from_single'),
    url(r'^deletesubscription/(?P<id>.*)/$', 'blogs.views.deletesubscription'),
    url(r'^deleteemail/(?P<id>.*)/$', 'blogs.views.deleteemail'),
    url(r'^deleteblog/(?P<slug>.*)/$', 'blogs.views.deleteblog'),
    url(r'^hot/(?P<id>.*)/$', 'punns.views.hot'),
    url(r'^up/(?P<id>.*)/$', 'votes.views.up'),
    url(r'^down/(?P<id>.*)/$', 'votes.views.down'),
    url(r'^comment-up/(?P<id>.*)/$', 'votes.views.commentup'),
    url(r'^comment-down/(?P<id>.*)/$', 'votes.views.commentdown'),
    url(r'^reblog/(?P<id>.*)/$', 'punns.views.reblog'),
    url(r'^favorite/(?P<id>.*)/$', 'punns.views.favorite'),
    url(r'^p/(?P<shorturl>.*)/$', 'blogs.views.single'),
    url(r'^a/(?P<shorturl>.*)/$', 'punns.views.album'),
    url(r'^privacy/$', direct_to_template, { 'template': 'privacy.html' }),
    url(r'^tos/$', direct_to_template, { 'template': 'tos.html' }),
    url(r'^opinion/$', direct_to_template, { 'template': 'opinion.html' }),
    url(r'^closed/$', direct_to_template, { 'template': 'closed.html' }),
    url(r'^privacypolicy/$', direct_to_template, { 'template': 'privacypolicy.html' }),
    url(r'^terms/$', direct_to_template, { 'template': 'terms.html' }),
    url(r'^billing/$', direct_to_template, { 'template': 'bill.html' }),
    url(r'^totb/$', direct_to_template, { 'template': 'totb.html' }),
    url(r'^totb_single/$', direct_to_template, { 'template': 'totb_single.html' }),
    url(r'^gabrieldancause/$', direct_to_template, { 'template': 'gabrieldancause.html' }),
    url(r'^c/(?P<shorturl>.)/$', 'punns.views.comment'),
    url(r'^s/$', 'punns.views.search'),
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
    url(r'^submit/$', 'blogs.views.submit'),
    url(r'^draft/$', 'blogs.views.draft'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
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
