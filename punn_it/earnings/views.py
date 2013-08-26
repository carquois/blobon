from earnings.models import Earning

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import datetime
from datetime import date, timedelta

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.db.models import Sum

from django.utils import timezone

@login_required
def index(request):
      if request.META['HTTP_HOST'] == settings.MAIN_SITE_DOMAIN:
        earnings = Earning.objects.filter(user=request.user).all()
        all_time = Earning.objects.filter(user=request.user).all().aggregate(total_earned=Sum('amount'))
        last_30_days = Earning.objects.filter(user=request.user).filter(date__range=(datetime.date.today() - timedelta(days=30) , datetime.date.today())).aggregate(total_earned=Sum('amount'))
        today = Earning.objects.filter(user=request.user).filter(date__gte=datetime.date.today()).aggregate(total_earned=Sum('amount'))
      else:
        error_msg = _("Looks like this domain is not configured. If you own it, you should add it in your settings")
        return HttpResponse('<p>%s</p>' % error_msg)
      return render_to_response('earnings.html',
                                {'earnings': earnings, 'all_time': all_time, 'last_30_days': last_30_days, 'today': today},
                                context_instance=RequestContext(request))



