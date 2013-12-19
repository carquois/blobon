# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _


from posts.forms import BlogPostForm
from posts.models import BlogPost

@login_required
def createblogpost(request):
#      if request.method == 'POST':
#        if request.POST['id_content']:
#            blog = BlogPost(author = request.user)
#            if request.POST['id_status']:
#              if request.POST['id_status'] == "P":
#                blog.status = "P"
#            else:
#              blog.status = "P"
#            blog.password = request.POST['propassword']
#          else:
#            blog.status = "Pu"
#          blog.save()
#
#
#        form = BlogPostForm(request.POST)
#        if form.is_valid():
#          blogpost = form.save(commit=False)
#          blogpost.author = request.user
#          blogpost.save()
#          messages.add_message(request, messages.INFO, _(u"The new entry has been created"))
#          return HttpResponseRedirect('/')
#      else:
#        form = BlogPostForm()
      return render_to_response('createblogpost.html',
                                {},
                                context_instance=RequestContext(request))


@login_required
def createimage(request):
      return render_to_response('dashboard.html',
                                {},
                                context_instance=RequestContext(request))


@login_required
def createalbum(request):
      return render_to_response('dashboard.html',
                                {},
                                context_instance=RequestContext(request))
