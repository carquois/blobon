from punns.models import Punn
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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): 
          form.save()
          return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render_to_response('signup.html', {
        'form': form,
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
          form.save()
          return HttpResponseRedirect('/')
    else:
        form = UserProfileForm()
    return render_to_response('edit_profile.html', {
        'form': form,
    })

def index(request): 
    latest_punn_list = Punn.objects.all().order_by('pub_date')[:24]
    current_site = Site.objects.get(id=settings.SITE_ID)
    return render_to_response('index.html', 
                              {'site': current_site, 'latest_punn_list': latest_punn_list}, 
                              context_instance=RequestContext(request))

def tag(request, shorturl):
    return HttpResponse("Tag page")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/fdsa/")
    else:
        return HttpResponseRedirect("/account/invalid/")

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def comment(request, shorturl):
    c = get_object_or_404(Comment, base62id=shorturl)
    latest_reply_list = Comment.objects.filter(parent=c.id).order_by('pub_date')[:6]
    return render_to_response('comment.html', {'comment': c, 'latest_reply_list': latest_reply_list})

def profile_page(request, user):
    u = get_object_or_404(User, username=user)
    current_site = Site.objects.get(id=settings.SITE_ID)
    latest_punn_list = Punn.objects.filter(author=u).order_by('pub_date')[:24]
    return render_to_response('profile.html', {'user': u, 'site': current_site, 'latest_punn_list': latest_punn_list})

#TODO enctype="multipart/form-data" dans le <form>
@login_required
def submit(request): 
    if request.method == 'POST': 
      title = request.POST.get('title', '')
      image = request.POST.get('image', '')
      source = request.POST.get('source', '')
      tags = request.POST.get('tags', '')
      return render_to_response('submit.html', {})
    elif request.method == 'GET':
      title = request.GET.get('title', '') 
      image = request.GET.get('image', '') 
      source = request.GET.get('source', '') 
      tags = request.GET.get('tags', '') 
      return render_to_response('submit.html', {'title': title, 'image': image, 'source': source, 'tags': tags})
    else:
      return render_to_response('submit.html', {})

def single(request, shorturl):
    current_site = Site.objects.get(id=settings.SITE_ID)
    p = get_object_or_404(Punn, base62id=shorturl)
    u = p.author
    latest_punn_list = Punn.objects.filter(pub_date__gt=p.pub_date).order_by('pub_date').exclude(pk=p.id)[:6]
    latest_repunn_list = Punn.objects.filter(original_punn=p.id).order_by('pub_date')[:6]
    top_comments = Comment.objects.all().order_by('karma')[:6]
    return render_to_response('single.html', {'punn': p, 'user': u,  'site': current_site, 'latest_punn_list': latest_punn_list, 'latest_repunn_list': latest_repunn_list, 'top_comments': top_comments}, context_instance=RequestContext(request))



