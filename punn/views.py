from punn.models import Punn
from punn.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def home(request):
    return HttpResponse("Hello index")

def detail(request, punn_id):
    p = get_object_or_404(Punn, pk=punn_id)
    return render_to_response('punn/index.html', {'punn': p})





