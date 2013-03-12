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
from accounts.forms import UserCreateForm, SocialSignupForm


def signup(request):
    if request.user.is_authenticated() and request.user.get_profile().is_new_from_social:
        return HttpResponseRedirect(reverse('accounts.views.social_signup_step2'))

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('punns.views.index'))
    
    
    return render_to_response("registration/signup.html", context_instance=RequestContext(request))
                                
def social_signup_step2(request):
    user = request.user
    
    if not user.is_authenticated():
        return HttpResponseRedirect(reverse('accounts.views.signup'))

    if user.is_authenticated() and not user.get_profile().is_new_from_social:
        return HttpResponseRedirect(reverse('punns.views.index'))

    if request.POST:
        form = SocialSignupForm(request.POST, request.FILES or None)
    else:
        form = SocialSignupForm(initial={
            'email' : user.email,
            'username' : user.username,
        })
    
    if form.is_valid():
        #set user fields
        user.username =  form.cleaned_data['username']
        user.set_password(form.cleaned_data['password']) 
        
        #dont save email... always use the one provided by Facebook
        # user.email = form.cleaned_data['email']
        user.save()
        
        profile = user.get_profile()
        profile.is_new_from_social = False
        
        #if there is a new uploaded avatar, we overwrite it 
        if form.cleaned_data['avatar']:
            profile.avatar= form.cleaned_data['avatar']
        
        
        profile.save()
        
        #send a welcome message to the templates
        messages.add_message(request, messages.INFO, _(u'Bienvenue sur Check Donc Ça!'))
        return HttpResponseRedirect(reverse('punns.views.index'))
    
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
        form = UserProfileForm(request.POST)
        if form.is_valid():
          form.save()
          return HttpResponseRedirect(reverse('punns.views.index'))
    else:
        form = UserProfileForm()
    return render_to_response('edit_profile.html', locals())

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))
