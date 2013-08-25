
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

@login_required
def index(request):
      if request.META['HTTP_HOST'] == settings.MAIN_SITE_DOMAIN::
          user = ""
          punns = paginate(request,
                           Punn.objects.filter(status='P').filter(is_top=True).order_by('-pub_date'),
                           15)
      else:
        return redirect("http://knobshare.com")
      return render_to_response('index.html',
                               {'user': user,
                                'punns': punns, },
                                context_instance=RequestContext(request))


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



