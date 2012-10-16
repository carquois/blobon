from cgi import parse_qs
import re
import markdown
from django.views.decorators.cache import cache_page
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
from django.http import HttpResponseRedirect, HttpResponseNotFound
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
import urlparse
from urlparse import urlparse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class UserFeed(Feed):
    def get_object(self, request, username):
        return get_object_or_404(User, username=username)
    def title(self, obj):
        return "%s" % obj.first_name 
    def link(self, obj):
          return "http://%s/%s" % ("http://checkdonc.ca", obj.get_absolute_url())
    def description(self, obj):
        return "Feed : %s" % obj.username
    def items(self, obj):
        return Punn.objects.filter(author=obj).filter(status='P').order_by('-pub_date')[:30]


def draft(request):
        host = request.META['HTTP_HOST']
        url = 'http://%s/' % (host) 
        if UserProfile.objects.filter(domain=url).exists():
          user = UserProfile.objects.get(domain=url).user
          home = user.userprofile.domain
          punn_list = Punn.objects.filter(author=user).filter(status='D').order_by('pub_date')
          paginator = Paginator(punn_list, 25)
          col = ['2', '3', '4']
          page = request.GET.get('page')
          try:
            punns = paginator.page(page)
          except PageNotAnInteger:
            punns = paginator.page(1)
          except EmptyPage:
            punns = paginator.page(paginator.num_pages)
          return render_to_response('profile.html', locals(), context_instance=RequestContext(request))
        else:
          punn_list = Punn.objects.filter(status='D').order_by('pub_date')
          return render_to_response('profile.html', locals(), context_instance=RequestContext(request))


def index(request): 
    host = request.META['HTTP_HOST']
    url = 'http://%s/' % (host)
    if UserProfile.objects.filter(domain=url).exists():
      user = UserProfile.objects.get(domain=url).user
      home = user.userprofile.domain
      punn_list = Punn.objects.filter(author=user).filter(status='P').order_by('-pub_date')
      paginator = Paginator(punn_list, 25)
      page = request.GET.get('page')
      try:
        punns = paginator.page(page)
      except PageNotAnInteger:
        punns = paginator.page(1)
      except EmptyPage:
        punns = paginator.page(paginator.num_pages)
      return render_to_response('profile.html', locals(), context_instance=RequestContext(request))
    else:
      punn_list = Punn.objects.filter(status='P').order_by('-pub_date')
      paginator = Paginator(punn_list, 25)
      page = request.GET.get('page')
      try:
        punns = paginator.page(page)
      except PageNotAnInteger:
        punns = paginator.page(1)
      except EmptyPage:
        punns = paginator.page(paginator.num_pages)
      return render_to_response('profile.html', locals(), context_instance=RequestContext(request))

@login_required
def comment(request, shorturl):
    comment = get_object_or_404(Comment, base62id=shorturl)
    latest_reply_list = Comment.objects.filter(parent=comment.id).order_by('pub_date')[:6]
    return render_to_response('comment.html', {'comment': comment, 'latest_reply_list': latest_reply_list}, context_instance=RequestContext(request))

@login_required
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
      user = get_object_or_404(User, username=user)
      if user.userprofile.domain:
        return HttpResponseRedirect(user.userprofile.domain)
      else:
        latest_punn_list = Punn.objects.filter(author=user).filter(status='P').annotate(number_of_comments=Count('comment')).order_by('-pub_date')[:100]
        return render_to_response('profile.html', locals(), context_instance=RequestContext(request))

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
          if request.POST['is_video'] == 'true':
            query = urlparse(new_punn.source)
            p = parse_qs(query.query)
            new_punn.youtube_id = p['v'][0]
            new_punn.save()
          return render_to_response('success.html', {"punn": new_punn}, context_instance=RequestContext(request))
    elif request.method == 'GET':
      source = request.GET.get('url', '') 
      title = request.GET.get('title', '') 
      image = request.GET.get('media', '') 
      is_video = request.GET.get('is_video', '') 
      form = PunnForm(initial={'source':source, 'title':title, 'image': image, 'is_video':is_video})
      return render_to_response('submit.html', locals(), context_instance=RequestContext(request))
    else:
      form = PunnForm()
    return render_to_response('submit.html', locals(), context_instance=RequestContext(request))

def single(request, shorturl):
    punn = get_object_or_404(Punn, base62id=shorturl)
    if request.user.is_authenticated():
      auth_user = request.user
    if punn.author.userprofile.domain:
      home = punn.author.userprofile.domain
    else:
      home = "http://checkdonc.ca"
    latest_punn_list = Punn.objects.filter(pub_date__lt=punn.pub_date).filter(author=punn.author).filter(status='P').order_by('-pub_date').exclude(pk=punn.id)[:6]
    next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]
    prev_punn = ""
    next_punn = ""
    if Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]:
      next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).filter(author=punn.author).filter(status='P').order_by('-pub_date').exclude(pk=punn.id)[:1]
      if (next_punn_query.count() > 0):
        next_punn = next_punn_query[0] 
    if Punn.objects.filter(pub_date__gt=punn.pub_date).order_by('pub_date').exclude(pk=punn.id)[:1]:
      prev_punn_query = Punn.objects.filter(pub_date__gt=punn.pub_date).filter(author=punn.author).filter(status='P').order_by('pub_date').exclude(pk=punn.id)[:1]
      if (prev_punn_query.count() > 0):
        prev_punn = prev_punn_query[0] 
    content = ""
    if punn.content:
        content = linkify(punn.content) 
        content = markdown.markdown(content)
    comment_list = Comment.objects.filter(punn=punn).order_by('-pub_date')
    url = request.build_absolute_uri()
    return render_to_response('single.html', {'punn': punn, 'latest_punn_list': latest_punn_list,
                                              'next_punn': next_punn, 'prev_punn': prev_punn, 
                                              'content': content, 'comment_list': comment_list,
                                              'url': url}, context_instance=RequestContext(request))


def linkify(string):
    string = re.sub(r'(\A|\s)@(\w+)', r'\1[@\2](/\2)', string)
    return re.sub(r'(\A|\s)#(\w+)', r'\1[#\2](/s/\2)', string)
