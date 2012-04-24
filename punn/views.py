from punn.models import Punn
from punn.models import UserProfile
from punn.models import Comment
from django.http import HttpResponse
from django.conf import settings
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

BASE10 = "0123456789"
BASE62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"


def index(request): 
    latest_punn_list = Punn.objects.all().order_by('pub_date')[:24]
    current_site = Site.objects.get(id=settings.SITE_ID)
    return render_to_response('index.html', {'site': current_site, 'latest_punn_list': latest_punn_list})

def tag(request, shorturl):
    return HttpResponse("Tag page")

def comment(request, shorturl):
    i = baseconvert(shorturl,BASE62,BASE10)
    c = get_object_or_404(Comment, pk=i)
    latest_reply_list = Comment.objects.filter(parent=c.id).order_by('pub_date')[:6]
    return render_to_response('comment.html', {'comment': c, 'latest_reply_list': latest_reply_list})

def profile_page(request, user):
    u = get_object_or_404(User, username=user)
    current_site = Site.objects.get(id=settings.SITE_ID)
    latest_punn_list = Punn.objects.filter(author=u).order_by('pub_date')[:24]
    return render_to_response('profile.html', {'user': u, 'site': current_site, 'latest_punn_list': latest_punn_list})

def submit(request): 
    if request.method == 'POST': 
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
    i = baseconvert(shorturl,BASE62,BASE10)
    p = get_object_or_404(Punn, pk=i)
    u = p.author
    latest_punn_list = Punn.objects.filter(pub_date__gt=p.pub_date).order_by('pub_date').exclude(pk=p.id)[:6]
    latest_repunn_list = Punn.objects.filter(original_punn=p.id).order_by('pub_date')[:6]
    top_comments = Comment.objects.all().order_by('karma')[:6]
    tag_cloud = p.tags.all()[:6]
    return render_to_response('single.html', {'punn': p, 'user': u,  'site': current_site, 'tag_cloud': tag_cloud, 'latest_punn_list': latest_punn_list, 'latest_repunn_list': latest_repunn_list, 'top_comments': top_comments})


def baseconvert(number,fromdigits,todigits):
    if str(number)[0]=='-':
        number = str(number)[1:]
        neg=1
    else:
        neg=0
    # make an integer out of the number
    x=0
    for digit in str(number):
       x = x*len(fromdigits) + fromdigits.index(digit)
    # create the result in base 'len(todigits)'
    if x == 0:
        res = todigits[0]
    else:
        res=""
        while x>0:
            digit = x % len(todigits)
            res = todigits[digit] + res
            x = int(x / len(todigits))
        if neg:
            res = "-"+res

    return res

