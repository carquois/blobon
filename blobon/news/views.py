# -*- coding: utf-8 -*-

from news.models import Post

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.sites.models import get_current_site

def all(request):
      news = Post.objects.all().order_by('-pub_date')
      site = get_current_site(request)
      return render_to_response('news.html',
                               {'news': news, 'site': site},
                                context_instance=RequestContext(request))

