
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
      if request.META['HTTP_HOST'] == "knobshare.com":
          user = ""
          punns = paginate(request,
                           Punn.objects.filter(status='P').filter(is_top=True).order_by('-pub_date'),
                           15)
      elif UserProfile.objects.filter(domain='http://%s/' % request.META['HTTP_HOST']).exists():
          user = UserProfile.objects.get(domain='http://%s/' % request.META['HTTP_HOST']).user
          punns = paginate(request,
                           Punn.objects.filter(author=user).filter(status='P').order_by('-pub_date'),
                           15)
      else:
        return redirect("http://knobshare.com")
      return render_to_response('index.html',
                               {'user': user,
                                'punns': punns, },
                                context_instance=RequestContext(request))



