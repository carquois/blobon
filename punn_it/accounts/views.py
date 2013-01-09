# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from accounts.forms import UserCreateForm

def signup(request):
    if request.user.is_authenticated():
      return HttpResponseRedirect(reverse('punns.views.index'))
    else:
      return render_to_response("registration/signup.html", 
                                context_instance=RequestContext(request))

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
