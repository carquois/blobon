# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _

from blogs.forms import BlogForm
from blogs.models import Blog

@login_required
def createblog(request):
      if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
          blog = form.save(commit=False)
          blog.creator = request.user
          if request.POST['propassword']:
            blog.status = "Pr"
            blog.password = request.POST['propassword']
          else:
            blog.status = "Pu"
          blog.save()
          messages.add_message(request, messages.INFO, _(u"Congratulation, you just created a blog"))
          return HttpResponseRedirect(reverse('blogs.views.administrateblog', args=(blog.slug,)))
      else:
        form = BlogForm()
      return render_to_response('createblog.html',
                                {'form': form},
                                context_instance=RequestContext(request))

@login_required
def administrateblog(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      return render_to_response('administrateblog.html',
                                {'blog': blog},
                                context_instance=RequestContext(request))

@login_required
def dashboard(request):
      return render_to_response('dashboard.html',
                                {'blog': blog},
                                context_instance=RequestContext(request))
