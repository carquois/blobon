# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _


from pages.forms import PageForm
from pages.models import Page
from blogs.models import Blog 

@login_required
def createpage(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
          page = form.save(commit=False)
          page.author = request.user
          if blog.creator == request.user:
            page.blog = blog
          page.save()
          messages.add_message(request, messages.INFO, _(u"Your page has been created"))
          return HttpResponseRedirect('/')
      else:
        form = PageForm()
      return render_to_response('createpage.html',
                                {'form': form, 'blog': blog},
                                context_instance=RequestContext(request))

