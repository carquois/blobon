# -*- coding: utf-8 -*-

import re
import markdown
import urllib2
from urlparse import urlparse
from cgi import parse_qs

from accounts.models import UserProfile, UserForm, UserProfileForm
from comments.models import Comment
from punns.models import Punn, PunnForm
from punns.utils import BASE10, BASE62, baseconvert
from votes.models import PunnVote

from django import forms
from django.conf import settings
from django.contrib import auth
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
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_page

def index(request, draft):
      #Affichage de checkdonc.ca
      user = UserProfile.objects.get(pk=3)
      #Test to see if the variable is a draft or not
      if draft == False:
        punns = paginate(request,
                         Punn.objects.filter(author=user).filter(status='P').order_by('-pub_date'),
                         20)
      else:
        punns = paginate(request,
                         Punn.objects.filter(author=user).filter(status='D').order_by('-pub_date'),
                         20)
      site_description = settings.MAIN_SITE_DESCRIPTION
      site = get_current_site(request)
      return render_to_response('profile.html',
                               {'user': user, 'site_description': site_description,
                                'punns': punns, 'site': site},
                               context_instance=RequestContext(request))

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
        return render_to_response('profile.html', { 'user': user, 'latest_punn_list':latest_punn_list}, context_instance=RequestContext(request))

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
    comment_list = Comment.objects.filter(punn=punn).order_by('-pub_date')
    for comment in comment_list:
        comment.content = linkify(comment.content)
        comment.content = markdown.markdown(comment.content)
    url = request.build_absolute_uri()
    check_mobile(request)
    if request.is_mobile:
      is_mobile = True
    else:
      is_mobile = False
    return render_to_response('single.html', 
                              {'punn': punn, 'latest_punn_list': latest_punn_list,
                               'next_punn': next_punn, 'prev_punn': prev_punn, 
                               'content': content, 'comment_list': comment_list,
                               'url': url, 'karma':karma, 'auth_user':auth_user,
                               'vote': vote, 'user': punn.author, 'home': home, 
                               'is_mobile': is_mobile}, 
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
#Une fonction pour vérifier si le l'utilisateur utilise unappareil mobile
def check_mobile(request): 
        is_mobile = False;

        if request.META.has_key('HTTP_USER_AGENT'):
            user_agent = request.META['HTTP_USER_AGENT']

            # Test common mobile values.
            pattern = "(up.browser|up.link|mmp|symbian|smartphone|midp|wap|phone|windows ce|pda|mobile|mini|palm|netfront)"
            prog = re.compile(pattern, re.IGNORECASE)
            match = prog.search(user_agent)

            if match:
                is_mobile = True;
            else:
                # Nokia like test for WAP browsers.
                # http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension

                if request.META.has_key('HTTP_ACCEPT'):
                    http_accept = request.META['HTTP_ACCEPT']

                    pattern = "application/vnd\.wap\.xhtml\+xml"
                    prog = re.compile(pattern, re.IGNORECASE)

                    match = prog.search(http_accept)

                    if match:
                        is_mobile = True

            if not is_mobile:
                # Now we test the user_agent from a big list.
                user_agents_test = ("w3c ", "acs-", "alav", "alca", "amoi", "audi",
                                    "avan", "benq", "bird", "blac", "blaz", "brew",
                                    "cell", "cldc", "cmd-", "dang", "doco", "eric",
                                    "hipt", "inno", "ipaq", "java", "jigs", "kddi",
                                    "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
                                    "maui", "maxo", "midp", "mits", "mmef", "mobi",
                                    "mot-", "moto", "mwbp", "nec-", "newt", "noki",
                                    "xda",  "palm", "pana", "pant", "phil", "play",
                                    "port", "prox", "qwap", "sage", "sams", "sany",
                                    "sch-", "sec-", "send", "seri", "sgh-", "shar",
                                    "sie-", "siem", "smal", "smar", "sony", "sph-",
                                    "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
                                    "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
                                    "wapi", "wapp", "wapr", "webc", "winw", "winw",
                                    "xda-",)

                test = user_agent[0:4].lower()
                if test in user_agents_test:
                    is_mobile = True

        request.is_mobile = is_mobile
        return request

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
    return re.sub(r'(\A|\s)#(\w+)', r'\1[#\2](/s/\2)', string)
