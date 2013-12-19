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
from punns.models import Punn, PunnForm, Reblog, Favorite, Cat
from punns.utils import BASE10, BASE62, baseconvert
from votes.models import PunnVote, CommentVote

from django import forms
from django.contrib.auth import authenticate, login
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


def attach_infos(punns):
      for punn in punns:
          votesup = PunnVote.objects.filter(punn=punn).filter(vote='U')
          votesdown = PunnVote.objects.filter(punn=punn).filter(vote='D')
          punn.score = votesup.count() - votesdown.count()
      return punns


def index(request):
      user = ""
      punns = paginate(request,
                       Punn.objects.filter(status='P').filter(is_top=True).annotate(number_of_comments=Count('comment')).order_by('-pub_date'),
                       15)
      punns = attach_infos(punns)
      latest_comments = Comment.objects.all().order_by('-created')[:5]
      cats = Cat.objects.filter(is_top_level=True)
      return render_to_response('index.html',
                               {'user': user, 'cats': cats,
                                'punns': punns, 'latest_comments': latest_comments},
                                context_instance=RequestContext(request))

def pics(request):
      user = ""
      punns = paginate(request,
                       Punn.objects.filter(status='P').filter(youtube_id="").annotate(number_of_comments=Count('comment')).order_by('-pub_date'),
                       15)
      punns = attach_infos(punns)
      latest_comments = Comment.objects.all().order_by('-created')[:5]
      cats = Cat.objects.filter(is_top_level=True)
      return render_to_response('index.html',
                               {'user': user, 'cats': cats,
                                'punns': punns, 'latest_comments': latest_comments},
                                context_instance=RequestContext(request))
def videos(request):
      user = ""
      punns = paginate(request,
                       Punn.objects.filter(status='P').filter(youtube_id!="").annotate(number_of_comments=Count('comment')).order_by('-pub_date'),
                       15)
      punns = attach_infos(punns)
      latest_comments = Comment.objects.all().order_by('-created')[:5]
      cats = Cat.objects.filter(is_top_level=True)
      return render_to_response('index.html',
                               {'user': user, 'cats': cats,
                                'punns': punns, 'latest_comments': latest_comments},
                                context_instance=RequestContext(request))


def new(request):
      punns = paginate(request,
                       Punn.objects.filter(status='P').annotate(number_of_comments=Count('comment')).order_by('-pub_date'),
                       15)
      punns = attach_infos(punns)
      return render_to_response('new.html',
                                {'punns': punns, },
                                context_instance=RequestContext(request))




def cat(request, slug):
      cat = get_object_or_404(Cat, slug=slug)
      cats = Cat.objects.filter(is_top_level=True)
      punns = paginate(request,
                       Punn.objects.filter(status='P').filter(cat=cat).annotate(number_of_comments=Count('comment')).order_by('-pub_date'),
                       15)
      punns = attach_infos(punns)
      return render_to_response('cat.html',
                                {'punns': punns, 'cat': cat, 'cats': cats},
                                context_instance=RequestContext(request))

@login_required
def hot(request, id):
      punn = get_object_or_404(Punn, id=id)
      if request.user.is_staff:
        if punn.is_top == True:
          punn.is_top = False 
          punn.save()
        else:
          punn.is_top = True
          punn.save();
      return HttpResponseRedirect( punn.get_absolute_url() )

@login_required
def delete(request, id):
      punn = get_object_or_404(Punn, id=id)
      if request.user == punn.author:
        punn.delete()
        messages.add_message(request, messages.INFO, _(u'Votre page a été supprimée'))
      elif request.user.is_staff:
        punn.delete()
        messages.add_message(request, messages.INFO, _(u'La page a été supprimée'))
      return HttpResponseRedirect(reverse('punns.views.index'))

@login_required
def reblog(request, id):
      punn = get_object_or_404(Punn, id=id)
      if Reblog.objects.filter(origin=punn).filter(author=request.user).exists():
        r = Reblog.objects.filter(origin=punn).filter(author=request.user)
        r.delete()
      else: 
        r = Reblog(origin=punn, author=request.user)
        r.save()
      return HttpResponseRedirect( punn.get_absolute_url() )

@login_required
def favorite(request, id):
      punn = get_object_or_404(Punn, id=id)
      if Favorite.objects.filter(punn=punn).filter(author=request.user).exists():
        f = Favorite.objects.filter(punn=punn).filter(author=request.user)
        f.delete()
      else:
        f = Favorite(punn=punn, author=request.user)
        f.save()
      return HttpResponseRedirect( punn.get_absolute_url() )

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

@login_required
def moderate(request):
      if request.user.is_staff:
        punns = paginate(request,
                         Punn.objects.exclude(author__is_staff=True).order_by('-pub_date'),
                         20)
      else:
        return HttpResponseRedirect(reverse('punns.views.index'))
      return render_to_response('base.html',
                                {'punns': punns, },
                                context_instance=RequestContext(request))
def draft(request):
      punns = paginate(request,
                       Punn.objects.filter(status='D').order_by('-pub_date'),
                       20)
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      return render_to_response('base.html',
                               {'site_description': site_description,
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

#def week(request):
#      punns = paginate(request,
#                       Punn.objects.filter(status='P').filter(pub_date__range=(datetime.date.today() - timedelta(days=7) , datetime.date.today())).order_by('-views'),
#                       20)
#      return render_to_response('top.html',
#                                {'site_description': site_description,
#                                 'punns': punns, 'site': site, 't': 'week'},
#                                context_instance=RequestContext(request))
#
#def month(request):
#      site = get_current_site(request)
#      punns = paginate(request,
#                       Punn.objects.filter(status='P').filter(pub_date__range=(datetime.date.today() - timedelta(days=30) , datetime.date.today())).order_by('-views'),
#                       20)
#      return render_to_response('top.html',
#                                {'site_description': site_description,
#                                 'punns': punns, 'site': site, 't': 'month'},
#                                context_instance=RequestContext(request))
#
#def top(request):
#      site = get_current_site(request)
#      punns = paginate(request,
#                       Punn.objects.filter(status='P').order_by('-views'),
#                       20)
#      return render_to_response('top.html',
#                                {'site_description': site_description,
#                                 'punns': punns, 'site': site, 't': 'all'},
#                                context_instance=RequestContext(request))
#
#def today(request):
#                       Punn.objects.filter(status='P').filter(pub_date__gte=datetime.date.today()).order_by('-views'),
#


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
        cats = Cat.objects.filter(is_top_level=True)
        punns = paginate(request,
                         Punn.objects.filter(author=user).filter(status='P').annotate(number_of_comments=Count('comment')).order_by('-pub_date'),
                         15)
        site_description = settings.MAIN_SITE_DESCRIPTION
        site = get_current_site(request)
        url = request.build_absolute_uri()

        from punns.forms import QuickPublish

        quick_publish = QuickPublish(request.POST, request.FILES or None)
        if request.user.is_authenticated() and quick_publish.is_valid():
          punn = quick_publish.save(commit=False)
          punn.author = request.user
          punn.status = "P"
          punn.save()
          #redirect user so a refresh doesn't trigger a double post
          return HttpResponseRedirect( punn.get_absolute_url() )


        return render_to_response('profile.html', 
                                  {'user': user, 'site_description': site_description, 'cats': cats,
                                   'site': site, 'punns': punns, 'url': url, 'quick_publish': quick_publish}, 
                                  context_instance=RequestContext(request))

@login_required
def createcat(request):
      from punns.models import CatForm
      if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
          cat = form.save(commit=False)
          cat.author = request.user
          cat.save()
          #heading = _(u"Your page has been published.")
          #message = _(u"You can now share it.")
          #messages.add_message(request, messages.INFO, '<h4 class="alert-heading">%s</h4><p>%s</p><p><a class="btn btn-primary" href="http://www.facebook.com/sharer.php?u=%s">Facebook</a> <a class="btn btn-primary" href="https://twitter.com/share?text=%s">Twitter</a></p>' % (heading , message, request.build_absolute_uri(punn.get_absolute_url()), punn.title), extra_tags='safe')
          return HttpResponseRedirect( cat.get_absolute_url() )
      else:
        form = CatForm()
      return render_to_response('createcat.html',
                                {'form': form},
                                context_instance=RequestContext(request))

@login_required
def create(request): 
      from punns.forms import PunnForm
      from earnings.models import Earning
      from datetime import datetime
      from decimal import Decimal
      if request.method == 'POST':
        form = PunnForm(request.POST, request.FILES)
        if form.is_valid():
          punn = form.save(commit=False)
          punn.author = request.user
          punn.status = "P"
          if request.user.is_staff:
            punn.is_top = True
          punn.save()
          e = Earning(user=request.user, amount=Decimal("0.02"), date=datetime.now())
          e.save()
          vote = PunnVote(punn=punn, user=request.user, vote='U')
          vote.save()
          if punn.publish_on_facebook:
            from social_auth.models import UserSocialAuth
            import facebook
            instance = UserSocialAuth.objects.filter(provider='facebook').filter(user=request.user)
            graph = facebook.GraphAPI(instance[0].tokens['access_token'])
            profile = graph.get_object("me")
            #Fix the link into something more kasher
            graph.put_object("me", "feed", message="%s http://%s%s" % (punn.title, settings.MAIN_SITE_DOMAIN, punn.get_absolute_url()))
          heading = _(u"Votre page est maintenant publiée.")
          message = _(u"Vous pouvez la partager.")
          messages.add_message(request, messages.INFO, '<h4 class="alert-heading">%s</h4><p>%s</p><p><a class="btn btn-primary" href="http://www.facebook.com/sharer.php?u=%s">Facebook</a> <a class="btn btn-primary" href="https://twitter.com/share?text=%s">Twitter</a></p>' % (heading , message, request.build_absolute_uri(punn.get_absolute_url()), punn.title), extra_tags='safe')
          return HttpResponseRedirect( punn.get_absolute_url() )
      else:
        form = PunnForm()
      return render_to_response('create.html', 
                                {'form': form}, 
                                context_instance=RequestContext(request))

@login_required
def create_from_rss(request): 
    if request.method == 'POST':
      punn = Punn(title=request.POST['title'], author=request.user, source=request.POST['source'])
      if request.user.is_staff:
          punn.is_top = True
      punn.status = "D"
      punn.save()
      img_temp = NamedTemporaryFile(delete=True)
      img_temp.write(urllib2.urlopen(request.POST['media']).read())
      img_temp.flush()
      filename = urlparse(request.POST['media']).path.split('/')[-1]
      ext = filename.split('.')[-1]
      prefix = punn.base62id
      filename = "%s.%s" % (prefix, ext)
      punn.pic.save(filename, File(img_temp))
      if request.POST['draft'] == "facebook":
        punn.status = "P"
        punn.save()
        from social_auth.models import UserSocialAuth
        import facebook
        import os
        instance = UserSocialAuth.objects.filter(provider='facebook').filter(user=request.user)
        graph = facebook.GraphAPI(instance[0].tokens['access_token'])
        os.chdir(settings.MEDIA_ROOT)
        response = graph.put_photo(open(str(punn.pic.name)), '%s\n\nhttp://%s%s' % (punn.title.encode('utf-8') , settings.MAIN_SITE_DOMAIN, punn.get_absolute_url() ))
        messages.add_message(request, messages.INFO, _(u"Votre image a été publiée <a href='https://www.facebook.com/photo.php?fbid=%s'>sur Facebook</a>" % response['id']), extra_tags='safe') 
      return HttpResponseRedirect( punn.get_absolute_url() )
    elif request.method == 'GET':
      if request.GET.get('url', ''):
        url = request.GET.get('url', '')
        import feedparser
        from BeautifulSoup import BeautifulSoup
        feed = feedparser.parse(url)
        parsed_feed = []
        for entry in feed.entries:
          response = urllib2.urlopen(entry.link)
          soup = BeautifulSoup(response.read())
          entry.img = []
          for image in soup.findAll("img"):
            entry.img.append(image['src'])
        return render_to_response('create-from-rss.html', 
                                  {'feed': feed, 'url': url, 'parsed_feed': parsed_feed}, 
                                  context_instance=RequestContext(request))
    return render_to_response('create-from-rss.html', 
                              {}, 
                              context_instance=RequestContext(request))


@login_required
def submit(request): 
    from punns.forms import SubmitForm
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
          new_punn = form.save(commit=False)
          new_punn.author = request.user
          if request.user.is_staff:
            new_punn.is_top = True
            new_punn.save()
          new_punn.status = "D"
          new_punn.save()
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
      form = SubmitForm(initial={'source':source, 'title':title, 'image': image, 'is_video':is_video})
      return render_to_response('submit.html', {'image': image, 'form': form, 'is_video': is_video}, context_instance=RequestContext(request))
    else:
      form = SubmitForm()
    return render_to_response('submit.html', {'form': form}, context_instance=RequestContext(request))

def single(request, shorturl):
    punn = get_object_or_404(Punn, base62id=shorturl)
    cats = Cat.objects.filter(is_top_level=True)
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
    latest_punn_list = Punn.objects.filter(pub_date__lt=punn.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=punn.id)[:6]
    next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]
    prev_punn = ""
    next_punn = ""
    if Punn.objects.filter(pub_date__lt=punn.pub_date).order_by('-pub_date').exclude(pk=punn.id)[:1]:
      next_punn_query = Punn.objects.filter(pub_date__lt=punn.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=punn.id)[:1]
      if (next_punn_query.count() > 0):
        next_punn = next_punn_query[0] 
    if Punn.objects.filter(pub_date__gt=punn.pub_date).order_by('pub_date').exclude(pk=punn.id)[:1]:
      prev_punn_query = Punn.objects.filter(pub_date__gt=punn.pub_date).filter(is_top=True).filter(status='P').order_by('pub_date').exclude(pk=punn.id)[:1]
      if (prev_punn_query.count() > 0):
        prev_punn = prev_punn_query[0] 
    content = ""
    if punn.content:
        content = linkify(punn.content) 
        content = markdown.markdown(content)
        
    #save new comment before querying for comments related to this punn
    comment_form = CommentForm(request.POST or None)
    if request.user.is_authenticated() and comment_form.is_valid():
        from earnings.models import Earning
        from datetime import datetime
        from decimal import Decimal
        comment = comment_form.save(commit=False)
        comment.punn = punn
        comment.author = request.user
        comment.save()
        vote = CommentVote(comment=comment, user=request.user, vote='U')
        vote.save()
        e = Earning(user=request.user, amount=Decimal("0.01"), date=datetime.now())
        e.save()
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


    if request.user.is_authenticated() and Reblog.objects.filter(origin=punn).filter(author=request.user).exists():
          reblog = True
    else:
          reblog = False 

    if request.user.is_authenticated() and Favorite.objects.filter(punn=punn).filter(author=request.user).exists():
          favorite = True
    else:
          favorite = False 


    url = request.build_absolute_uri()
    site_description = settings.MAIN_SITE_DESCRIPTION
    site = get_current_site(request)
    return render_to_response('single.html', 
                              {'punn': punn, 'latest_punn_list': latest_punn_list,
                               'next_punn': next_punn, 'prev_punn': prev_punn, 
                               'content': content, 'comment_list': comment_list,
                               'url': url, 'karma':karma, 'auth_user':auth_user,
                               'vote': vote, 'user': punn.author, 'home': home, 
                               'site_description': site_description, 'site': site, 'cats': cats, 
                               'comment_form': comment_form, 'reblog': reblog, 'favorite': favorite}, 
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
