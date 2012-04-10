from punn.models import Punn
from punn.models import User
from punn.models import Comment
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

BASE10 = "0123456789"
BASE62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"




def index(request):
    return HttpResponse("Hello index")

def detail(request, shorturl):
    print shorturl
    i = baseconvert(shorturl,BASE62,BASE10)
    p = get_object_or_404(Punn, pk=i)
    latest_punn_list = Punn.objects.filter(pub_date__gt=p.pub_date).order_by('pub_date').exclude(pk=p.id)[:6]
    latest_repunn_list = Punn.objects.filter(original_punn=p.id).order_by('pub_date')[:6]
    top_comments = Comment.objects.all().order_by('karma')[:6]
    tag_cloud = p.tags.all()[:6]
    return render_to_response('punn/single.html', {'punn': p, 'tag_cloud': tag_cloud, 'latest_punn_list': latest_punn_list, 'latest_repunn_list': latest_repunn_list, 'top_comments': top_comments})


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

