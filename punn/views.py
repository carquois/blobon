from punn.models import Punn
from punn.models import User
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
    return render_to_response('punn/index.html', {'punn': p})

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

