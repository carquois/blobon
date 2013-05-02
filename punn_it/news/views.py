# -*- coding: utf-8 -*-

from news.models import Post

from django.shortcuts import render_to_response
from django.template import RequestContext

def all(request):
      news = Post.objects.all().order_by('-pub_date')
      return render_to_response('news.html',
                               {'news': news},
                                context_instance=RequestContext(request))

