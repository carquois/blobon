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
        page = Page(author = request.user)
        page.blog = blog
        if request.POST['id_status']:
          if request.POST['id_status'] == "P":
            page.status = "P"
          else:
            page.status = "D"
        if request.POST['id_content']:
          page.content = request.POST['id_content']
        if request.POST['id_title']:
          page.title = request.POST['id_title']
        page.save()
        messages.add_message(request, messages.INFO, _(u"Your page has been created"))
        return HttpResponseRedirect('/')
      else:
        return render_to_response('createpage.html',
                                  {'blog': blog},
                                  context_instance=RequestContext(request))

