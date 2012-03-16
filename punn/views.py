from django.http import HttpResponse

def index(request):
    return HttpResponse("Page d'accueil")

def detail(request, punn_id):
    return HttpResponse("Affichage du punn %s." % punn_id)
