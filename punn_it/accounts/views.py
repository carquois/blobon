# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from accounts.forms import UserCreateForm, SocialSignupForm, UserProfileForm, UserForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import login

from twython import Twython

APP_KEY = 'rNUqZzZRzkwoPaXYytpFgQ'
APP_SECRET = 'CeDVT0e35vbs2KUBzQq6tQijdUfC4NL3XRmO12ZDyeA'


def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('punns.views.index'))
    else:
        return login(request)

@login_required
def twitter(request):
    twitter = Twython(APP_KEY, APP_SECRET)
    auth = twitter.get_authentication_tokens(callback_url='http://%s/twitter-success' % settings.MAIN_SITE_DOMAIN)
    request.session['oauth_token'] = auth['oauth_token']
    request.session['oauth_token_secret'] = auth['oauth_token_secret']
    return HttpResponseRedirect(auth['auth_url'])

@login_required
def twitter_success(request):
    twitter = Twython(APP_KEY, APP_SECRET, request.session['oauth_token'], request.session['oauth_token_secret'])
    final_step = twitter.get_authorized_tokens(request.GET.get("oauth_verifier", None))
    user = request.user
    profile = user.get_profile()
    profile.twitter_oauth_token = final_step['oauth_token'] 
    profile.twitter_oauth_token_secret = final_step['oauth_token_secret'] 
    profile.save()
    twitter = Twython(APP_KEY, APP_SECRET,
                  profile.twitter_oauth_token, profile.twitter_oauth_token_secret)
    response = twitter.verify_credentials()
    profile.twitter_link = "https://twitter.com/%s" % response['screen_name']
    profile.save()
    messages.add_message(request, messages.INFO, _(u'Votre compte Twitter @%s a été associé.') % response['screen_name'])
    return HttpResponseRedirect(reverse('punns.views.profile_page', args=[request.user.username]))

def signup(request):
    if request.user.is_authenticated() and request.user.get_profile().is_new_from_social:
        return HttpResponseRedirect(reverse('accounts.views.social_signup_step2'))

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('punns.views.index'))

    context = {}
    if request.GET.get("message", False):
        context.update({'error' : True})
    
    return render_to_response("registration/signup.html", context, context_instance=RequestContext(request))


def new_association(request):
    heading = _(u"Bravo!")
    message = _(u"Un nouveau compte a été associé.")
    messages.add_message(request, messages.INFO, "<strong>%s</strong> %s @%s" % (heading , message, request.user.username), extra_tags='safe')
    return HttpResponseRedirect(reverse('punns.views.profile_page', args=[request.user.username]))
                                
def social_signup_step2(request):
    user = request.user
    profile = user.get_profile()
    profile.is_new_from_social = False
    profile.save()
    #send a welcome message to the templates
    heading = _(u"Bienvenue")
    message = _(u"Votre nom d'utilisateur est :")
    messages.add_message(request, messages.INFO, "<strong>%s</strong> %s @%s" % (heading , message, request.user.username), extra_tags='safe')
    return HttpResponseRedirect(reverse('punns.views.profile_page', args=[request.user.username]))
#    
#    return render_to_response("registration/signup_social_step2.html", {'form': form,}, context_instance=RequestContext(request))
#    user = request.user
#    
#    if not user.is_authenticated():
#        return HttpResponseRedirect(reverse('accounts.views.signup'))
#
#    if user.is_authenticated() and not user.get_profile().is_new_from_social:
#        return HttpResponseRedirect(reverse('punns.views.index'))
#
#    if request.POST:
#        form = SocialSignupForm(request.POST, request.FILES or None)
#    else:
#        form = SocialSignupForm(initial={
#            'email' : user.email,
#            'username' : user.username,
#        })
#    
#    if form.is_valid():
#        #set user fields
#        user.username =  form.cleaned_data['username']
#        user.set_password(form.cleaned_data['password']) 
#        
#        #dont save email... always use the one provided by Facebook
#        # user.email = form.cleaned_data['email']
#        user.save()
#        
#        profile = user.get_profile()
#        profile.is_new_from_social = False
#        
#        #if there is a new uploaded avatar, we overwrite it 
#        if form.cleaned_data['avatar']:
#            profile.avatar= form.cleaned_data['avatar']
#        
#        profile.save()
#        
#        #send a welcome message to the templates
#        messages.add_message(request, messages.INFO, _(u'Bienvenue sur Check Donc Ça!'))
#        return HttpResponseRedirect(reverse('punns.views.index'))
#    
    return render_to_response("registration/signup_social_step2.html", {'form': form,}, context_instance=RequestContext(request))
    

def discover(request):
    return render_to_response("registration/discover.html", 
                              {}, 
                              context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
           new_user = form.save()
           return HttpResponseRedirect(reverse('accounts.views.discover'))
    else:
       form = UserCreateForm()
    return render_to_response("registration/register.html", {'form': form,}, context_instance=RequestContext(request))

@login_required
def edit_profile(request):
    if request.method == 'POST':
        userprofile_form = UserProfileForm(request.POST, instance=request.user.get_profile())
        user_form = UserForm(request.POST, instance=request.user)
        if userprofile_form.is_valid() and user_form.is_valid():
          userprofile_form.save()
          user_form.save()
          messages.add_message(request, messages.INFO, _(u"Merci. Vos paramètres ont été enregistrés."))
          return HttpResponseRedirect(reverse('accounts.views.edit_profile'))
    else:
        userprofile_form = UserProfileForm(instance=request.user.get_profile())
        user_form = UserForm(instance=request.user)
    return render_to_response('edit_profile.html', 
                              {'userprofile_form': userprofile_form, 'user_form': user_form}, 
                              context_instance=RequestContext(request))

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))
