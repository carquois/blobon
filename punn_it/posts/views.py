# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _


from posts.forms import BlogPostForm
from posts.models import BlogPost, Album, Link, Post

#class Post(models.Model):
#    author = models.ForeignKey(User, null=True)
#    created = models.DateTimeField(auto_now_add = True)
#    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
#
#class Image(Post):
#    status = models.CharField(max_length=2, choices=STATUS, null=True, blank=True)
#    title = models.CharField(verbose_name=_("Titre"), max_length=140, blank=True)
#    base62id = models.CharField(max_length=140, blank=True)
#    slug = models.SlugField(max_length=140, blank=True)
#    pic = ImageField(verbose_name=_("Image"), upload_to=get_file_path, null=True, blank=True)
#    def __unicode__(self):
#        return self.title

@login_required
def createimage(request):
      if request.FILES.get('id_album_1_image_1', False) and request.FILES.get('id_album_1_image_2', False):
        messages.add_message(request, messages.INFO, _(u"album a deux images"))
        if request.POST.get('id_title', False):
          title = request.POST.get('id_title')
#        image1 = Image(author=request.user)
#        image1.save()
#        f1 = request.FILES['id_album_1_image_1']
#        album_1_image_2 = request.FILES['id_album_1_image_2']
         
#        return HttpResponseRedirect("/")
      elif request.POST.get('id_album_2_image_1', False) and request.POST.get('id_album_2_image_2', False) and request.POST.get('id_album_2_image_3', False) and request.POST.get('id_album_2_image_4', False):
        messages.add_message(request, messages.INFO, _(u"album a 4 images"))
      elif request.POST.get('id_album_3_image_1', False) and request.POST.get('id_album_3_image_2', False) and request.POST.get('id_album_3_image_3', False) and request.POST.get('id_album_3_image_4', False) and request.POST.get('id_album_3_image_5', False) and request.POST.get('id_album_3_image_6', False):
        messages.add_message(request, messages.INFO, _(u"album a 6 images"))
      else:
        messages.add_message(request, messages.INFO, _(u"what t f"))
      return render_to_response('dashboard.html',
                                {},
                                context_instance=RequestContext(request))


@login_required
def createalbum(request):
      post = request.POST
      return render_to_response('dashboard.html',
                                {'post': post},
                                context_instance=RequestContext(request))

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
