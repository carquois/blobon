from punn.models import Punn
from punn.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    latest_punn_list = Punn.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('punn/index.html')
#    c = Context({
#        'latest_punn_list': latest_punn_list,
#    })
#    return HttpResponse(t.render(c))
    return render_to_response('punn/index.html', {'latest_punn_list': latest_punn_list})


def detail(request, punn_id):
    return HttpResponse("Affichage du punn %s." % punn_id)
