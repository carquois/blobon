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
    heading = _(u"Congratulations!")
    message = _(u"A new account has been associated.")
    messages.add_message(request, messages.INFO, "<strong>%s</strong> %s @%s" % (heading , message, request.user.username), extra_tags='safe')
    return HttpResponseRedirect(reverse('punns.views.profile_page', args=[request.user.username]))
                                
def social_signup_step2(request):
    user = request.user
    profile = user.get_profile()
    profile.is_new_from_social = False
    profile.save()
    #send a welcome message to the templates
    heading = _(u"Welcome to Knobshare")
    message = _(u"Your username has been set to :")
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
          messages.add_message(request, messages.INFO, _(u"Thank you! Your settings have been changed."))
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
