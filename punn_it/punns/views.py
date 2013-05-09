# -*- coding: utf-8 -*-

import datetime
from datetime import date, timedelta
import re
import markdown
import urllib2
from urlparse import urlparse
from cgi import parse_qs

from accounts.models import UserProfile, UserForm
from comments.models import Comment
from comments.forms import CommentForm
from punns.models import Punn, PunnForm
from punns.utils import BASE10, BASE62, baseconvert
from votes.models import PunnVote, CommentVote

from django import forms
from django.conf import settings
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.models import Site
from django.contrib.sites.models import get_current_site
from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.core.urlresolvers import reverse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page

def index(request):
      if request.META['HTTP_HOST'] != "checkdonc.ca":
        if UserProfile.objects.filter(domain='http://%s/' % request.META['HTTP_HOST']).exists():
          user = UserProfile.objects.get(domain='http://%s/' % request.META['HTTP_HOST']).user
        else:
          user = User.objects.get(pk=3)
      else:
        user = User.objects.get(pk=3)
      punns = paginate(request,
                       Punn.objects.filter(author=user).filter(status='P').order_by('-pub_date'),
                       20)
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      return render_to_response('base.html',
                               {'user': user, 'site_description': site_description,
                                'punns': punns, 'site': site},
                                context_instance=RequestContext(request))

def videos(request):
      user = UserProfile.objects.get(pk=3)
      punns = paginate(request,
                       Punn.objects.filter(author=user).filter(status='P').exclude(youtube_id__isnull=True).exclude(youtube_id='').order_by('-pub_date'),
                       20)
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      auth_user = ""
      if request.user.is_authenticated():
        auth_user = request.user
      return render_to_response('base.html',
                               {'user': user, 'site_description': site_description,
                                'punns': punns, 'site': site, 'auth_user': auth_user},
                                context_instance=RequestContext(request))



def draft(request):
      user = UserProfile.objects.get(pk=3)
      punns = paginate(request,
                       Punn.objects.filter(author=user).filter(status='D').order_by('-pub_date'),
                       20)
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      return render_to_response('base.html',
                               {'user': user, 'site_description': site_description,
                                'punns': punns, 'site': site},
                                context_instance=RequestContext(request))



def search(request):
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        user = UserProfile.objects.get(pk=3)
        punns = paginate(request,
                         Punn.objects.filter(title__icontains=q).filter(status='P').filter(author=user).order_by('-pub_date'),
                         20)
        return render_to_response('search.html',
                                  {'site_description': site_description, 'query': q,
                                   'punns': punns, 'site': site},
                                  context_instance=RequestContext(request))
      else:
        return HttpResponseRedirect('http://%s/' % site.domain)

def today(request):
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      punns = paginate(request,
                       Punn.objects.filter(status='P').filter(pub_date__gte=datetime.date.today()).order_by('-views'),
                       20)
      return render_to_response('top.html',
                                {'site_description': site_description,
                                 'punns': punns, 'site': site, 't': 'today'},
                                context_instance=RequestContext(request))

def week(request):
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      punns = paginate(request,
                       Punn.objects.filter(status='P').filter(pub_date__range=(datetime.date.today() - timedelta(days=7) , datetime.date.today())).order_by('-views'),
                       20)
      return render_to_response('top.html',
                                {'site_description': site_description,
                                 'punns': punns, 'site': site, 't': 'week'},
                                context_instance=RequestContext(request))

def month(request):
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      punns = paginate(request,
                       Punn.objects.filter(status='P').filter(pub_date__range=(datetime.date.today() - timedelta(days=30) , datetime.date.today())).order_by('-views'),
                       20)
      return render_to_response('top.html',
                                {'site_description': site_description,
                                 'punns': punns, 'site': site, 't': 'month'},
                                context_instance=RequestContext(request))

def top(request):
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      punns = paginate(request,
                       Punn.objects.filter(status='P').order_by('-views'),
                       20)
      return render_to_response('top.html',
                                {'site_description': site_description,
                                 'punns': punns, 'site': site, 't': 'all'},
                                context_instance=RequestContext(request))


def random(request):
      user = UserProfile.objects.get(pk=3)
      r = Punn.objects.filter(author=user).filter(status='P').order_by('?')[:1]
      return redirect(r[0])

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
      punns = paginate(request,
                       Punn.objects.filter(author=user).filter(status='P').annotate(number_of_comments=Count('comment')).order_by('-pub_date'),
                       20)
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      url = request.build_absolute_uri()
      return render_to_response('profile.html', 
                                {'user': user, 'site_description': site_description,
                                 'site': site, 'punns': punns, 'url': url}, 
                                context_instance=RequestContext(request))

@login_required
def create(request): 
      from punns.forms import PunnForm
      if request.method == 'POST':
        form = PunnForm(request.POST, request.FILES)
        if form.is_valid():
          punn = form.save(commit=False)
          punn.author = request.user
          punn.status = "P"
          punn.save()
          heading = _(u"Félicitations! Votre contenu est maintenant publié.")
          message = _(u"Vous pouvez dorénavant le partager")
          messages.add_message(request, messages.INFO, '<h4 class="alert-heading">%s</h4><p>%s</p><p><a class="btn btn-primary" href="http://www.facebook.com/sharer.php?u=%s">Facebook</a> <a class="btn" href="https://twitter.com/share?text=%s">Twitter</a></p>' % (heading , message, request.build_absolute_uri(punn.get_absolute_url()), punn.title), extra_tags='safe')
          return HttpResponseRedirect( punn.get_absolute_url() )
      else:
        form = PunnForm()
      return render_to_response('create.html', 
                                {'form': form}, 
                                context_instance=RequestContext(request))

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
      return render_to_response('submit.html', {'image': image, 'form': form, 'is_video': is_video}, context_instance=RequestContext(request))
    else:
      form = PunnForm()
    return render_to_response('submit.html', {'form': form}, context_instance=RequestContext(request))

def single(request, shorturl):
    punn = get_object_or_404(Punn, base62id=shorturl)
    votesup = PunnVote.objects.filter(punn=punn).filter(vote='U')
    votesdown = PunnVote.objects.filter(punn=punn).filter(vote='D')
    karma = votesup.count() - votesdown.count()
    auth_user = ""
    vote = ""
    if request.user.is_authenticated():
      auth_user = request.user
      if PunnVote.objects.filter(punn=punn).filter(user=auth_user):
        if PunnVote.objects.filter(punn=punn).filter(user=auth_user).filter(vote='U'):
          vote = 'U'
        else:
          vote = 'D'
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
        
    #save new comment before querying for comments related to this punn
    comment_form = CommentForm(request.POST or None)
    if request.user.is_authenticated() and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.punn = punn
        comment.author = request.user
        comment.save()
        #redirect user so a refresh doesn't trigger a double post
        return HttpResponseRedirect( punn.get_absolute_url() )
        

    comment_list = Comment.objects.filter(punn=punn).order_by('-pub_date')
    for comment in comment_list:
        comment.content = linkify(comment.content)
        comment.content = markdown.markdown(comment.content)
        votesup = CommentVote.objects.filter(comment=comment).filter(vote='U')
        votesdown = CommentVote.objects.filter(comment=comment).filter(vote='D')
        comment.karma = votesup.count() - votesdown.count()
       
        if request.user.is_authenticated() and CommentVote.objects.filter(comment=comment).filter(user=request.user).exists():
          v = CommentVote.objects.filter(comment=comment).filter(user=request.user)
          if v[0].vote == "U":
            comment.vote = "U"
          elif v[0].vote == "D":
            comment.vote = "D"


    url = request.build_absolute_uri()
    site_description = settings.MAIN_SITE_DESCRIPTION
    site = get_current_site(request)
    
    
    return render_to_response('single.html', 
                              {'punn': punn, 'latest_punn_list': latest_punn_list,
                               'next_punn': next_punn, 'prev_punn': prev_punn, 
                               'content': content, 'comment_list': comment_list,
                               'url': url, 'karma':karma, 'auth_user':auth_user,
                               'vote': vote, 'user': punn.author, 'home': home, 
                               'site_description': site_description, 'site': site, 'comment_form': comment_form}, 
                              context_instance=RequestContext(request))

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


###UTILS###
#Une fonction pour paginer une liste d'objets
def paginate(request, list_of_objects, number_of_items): 
    paginator = Paginator(list_of_objects, number_of_items)
    page = request.GET.get('page')
    try:
      paginated_objects = paginator.page(page)
    except PageNotAnInteger:
      paginated_objects = paginator.page(1)
    except EmptyPage:
      paginated_objects = paginator.page(paginator.num_pages)
    return paginated_objects

#Une fonction pour changer les usernames et les hastags en liens
def linkify(string):
    string = re.sub(r'(\A|\s)@(\w+)', r'\1[@\2](/\2)', string)
    return re.sub(r'(\A|\s)#(\w+)', r'\1[#\2](/s/?q=%23\2)', string)
