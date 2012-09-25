from django.contrib.auth.models import User
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
from django.contrib.syndication.views import Feed
from django.contrib.syndication.views import FeedDoesNotExist
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib2
from urlparse import urlparse

class UserFeed(Feed):
    #description_template = 'feeds.html'

    def get_object(self, request, username):
        return get_object_or_404(User, username=username)

    def title(self, obj):
        return "%s" % obj.first_name 

    def link(self, obj):
        if obj.userprofile.domain:
          return "http://%s/%s" % (obj.userprofile.domain, obj.get_absolute_url())
        else:
          return obj.get_absolute_url()

    def description(self, obj):
        return "Recent blobs by %s" % obj.username

    def items(self, obj):
        return Punn.objects.filter(author=obj).filter(status='P').order_by('-pub_date')[:30]

class LatestEntriesFeed(Feed):
    title = "Blobon"
    link = "/"
    description = "The World Rocks"

    def items(self):
      return Punn.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
      return item.title

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           new_user = form.save()
	   return HttpResponseRedirect(reverse('punns.views.edit_profile'))
    else:
       form = UserCreationForm()
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

def index(request): 
    host = request.META['HTTP_HOST']
    url = 'http://%s/' % (host)
    if host == 'blobon.com':
        home = "http://blobon.com"
        latest_punn_list = Punn.objects.annotate(number_of_comments=Count('comment')).order_by('-pub_date')[:100]
        return render_to_response('index.html', locals(), context_instance=RequestContext(request))
    else:
        if UserProfile.objects.filter(domain=url).exists():
          user = UserProfile.objects.get(domain=url).user
          home = user.userprofile.domain
          latest_punn_list = Punn.objects.filter(author=user).filter(status='P').annotate(number_of_comments=Count('comment')).order_by('-pub_date')[:100]
          return render_to_response('profile.html', locals(), context_instance=RequestContext(request))
        else:
          return HttpResponseRedirect('http://blobon.com') 

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

def comment(request, shorturl):
    comment = get_object_or_404(Comment, base62id=shorturl)
    latest_reply_list = Comment.objects.filter(parent=comment.id).order_by('pub_date')[:6]
    return render_to_response('comment.html', locals())

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        """Login complete view, displays user data"""
        ctx = {
            'last_login': request.session.get('social_auth_last_login_backend')
        }
        return render_to_response('done.html', ctx, RequestContext(request))
    else:
        return render_to_response('home.html', RequestContext(request))


@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {
        'last_login': request.session.get('social_auth_last_login_backend')
    }
    return render_to_response('done.html', ctx, RequestContext(request))

def profile_page(request, user):
    host = request.META['HTTP_HOST']
    url = 'http://%s/' % (host)
    slug = request.path
    if host == 'blobon.com':
      user = get_object_or_404(User, username=user)
      if user.userprofile.domain:
        return HttpResponseRedirect(user.userprofile.domain)
      else:
        latest_punn_list = Punn.objects.filter(author=user).annotate(number_of_comments=Count('comment')).order_by('-pub_date')[:100]
        return render_to_response('index.html', locals(), context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect('http://%s/' % (slug))

@login_required
def submit(request): 
    if request.method == 'POST':
        form = PunnForm(request.POST)
        if form.is_valid():
          new_punn = form.save()
          new_punn.source = request.POST['source']
          img_temp = NamedTemporaryFile(delete=True)
          img_temp.write(urllib2.urlopen(request.POST['media']).read())
          img_temp.flush()
          filename = urlparse(request.POST['media']).path.split('/')[-1]
          ext = filename.split('.')[-1]
          prefix = new_punn.base62id
          filename = "%s.%s" % (prefix, ext)
          new_punn.pic.save(filename, File(img_temp))
          return render_to_response('success.html', {"punn": new_punn}, context_instance=RequestContext(request))
          #return HttpResponseRedirect(reverse('punns.views.single', new_punn.base62id))
        #else:
        #  return render_to_response('submit.html', context_instance=RequestContext(request))
    elif request.method == 'GET':
      source = request.GET.get('url', '') 
      title = request.GET.get('title', '') 
      image = request.GET.get('media', '') 
      form = PunnForm(initial={'source':source, 'title':title, 'image': image})
      #page = urllib2.urlopen("http://imgur.com/gallery/K84kO")
      #soup = BeautifulSoup(page)
      #images = [] 
      #size = [] 
      #for image in soup.find_all('img'):
        #url = image.get('src')
        #usock = urllib2.urlopen(url)
        #data = usock.read()
        #size.append(data.__len__())
        #images.append(image.get('src'))
      #imagedata = soup.find_all('img')
      return render_to_response('submit.html', locals(), context_instance=RequestContext(request))
    else:
      form = PunnForm()
    return render_to_response('submit.html', locals(), context_instance=RequestContext(request))


def single(request, shorturl):
    punn = get_object_or_404(Punn, base62id=shorturl)
    user = punn.author
    if user.userprofile.domain:
      home = user.userprofile.domain
    else:
      home = "http://blobon.com"
    latest_punn_list = Punn.objects.filter(pub_date__lt=punn.pub_date).filter(author=user).filter(status='P').order_by('-pub_date').exclude(pk=punn.id)[:6]
    next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]
    if Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]:
      next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).filter(author=user).filter(status='P').order_by('-pub_date').exclude(pk=punn.id)[:1]
      if (next_punn_query.count() > 0):
        next_punn = next_punn_query[0] 
    if Punn.objects.filter(pub_date__gt=punn.pub_date).order_by('pub_date').exclude(pk=punn.id)[:1]:
      prev_punn_query = Punn.objects.filter(pub_date__gt=punn.pub_date).filter(author=user).filter(status='P').order_by('pub_date').exclude(pk=punn.id)[:1]
      if (prev_punn_query.count() > 0):
        prev_punn = prev_punn_query[0] 
    latest_repunn_list = Punn.objects.filter(original_punn=punn.id).order_by('pub_date')[:6]
    top_comments = Comment.objects.all().order_by('karma')[:6]
    url = request.build_absolute_uri()
    return render_to_response('single.html', locals(), context_instance=RequestContext(request))


def singletest(request, shorturl):
    punn = get_object_or_404(Punn, base62id=shorturl)
    latest_punn_list = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:6]
    next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]
    if Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]:
      next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]
      next_punn = next_punn_query[0]
    if Punn.objects.filter(pub_date__gt=punn.pub_date).order_by('pub_date').exclude(pk=punn.id)[:1]:
      prev_punn_query = Punn.objects.filter(pub_date__gt=punn.pub_date).order_by('pub_date').exclude(pk=punn.id)[:1]
      prev_punn = prev_punn_query[0]
    latest_repunn_list = Punn.objects.filter(original_punn=punn.id).order_by('pub_date')[:6]
    top_comments = Comment.objects.all().order_by('karma')[:6]
    return render_to_response('singletest.html', locals(), context_instance=RequestContext(request))

