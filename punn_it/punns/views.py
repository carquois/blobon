from punns.models import Punn, PunnForm
from accounts.models import UserProfile
from comments.models import Comment
from punns.utils import BASE10, BASE62, baseconvert
from accounts.models import UserForm
from accounts.models import UserProfileForm
from django.http import HttpResponse
from django.conf import settings
from django.contrib import auth
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Count
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           new_user = form.save()
	   return HttpResponseRedirect(reverse('punns.views.edit_profile'))
    else:
       form = UserCreationForm()
    return render_to_response("registration/register.html", {'form': form,}, context_instance=RequestContext(request))


def top(request):
    return render_to_response('top.html', locals(), context_instance=RequestContext(request))

def top_day(request):
    return HttpResponse('<h1>DAy</h1>')

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

def index(request): 
    latest_punn_list = Punn.objects.annotate(number_of_comments=Count('comment')).order_by('-pub_date')[:100]
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def tag(request, shorturl):
    return HttpResponse("Tag page")

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

def comment(request, shorturl):
    comment = get_object_or_404(Comment, base62id=shorturl)
    latest_reply_list = Comment.objects.filter(parent=comment.id).order_by('pub_date')[:6]
    return render_to_response('comment.html', locals())

def profile_page(request, user):
    user = get_object_or_404(User, username=user)
    site = Site.objects.get(id=settings.SITE_ID)
    latest_punn_list = Punn.objects.filter(author=user).order_by('-pub_date')[:24]
    return render_to_response('profile.html', locals(),context_instance=RequestContext(request))

@login_required
def submit(request): 
    if request.method == 'POST':
        form = PunnForm(request.POST)
        new_punn = form.save()
        new_punn.save()
        return HttpResponseRedirect(reverse('punns.views.single', shorturl=new_punn.base62id))
    elif request.method == 'GET':
      title = request.GET.get('title', '') 
      source = request.GET.get('source', '') 
      selection = request.GET.get('selection', '') 
      i = request.GET.get('i', '') 
      return render_to_response('submit.html', locals(), context_instance=RequestContext(request))
    else:
      return render_to_response('submit.html', {})

def single(request, shorturl):
    punn = get_object_or_404(Punn, base62id=shorturl)
    user = punn.author
    latest_punn_list = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:6]
    prev = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]
    latest_repunn_list = Punn.objects.filter(original_punn=punn.id).order_by('pub_date')[:6]
    top_comments = Comment.objects.all().order_by('karma')[:6]
    return render_to_response('single.html', locals(), context_instance=RequestContext(request))



