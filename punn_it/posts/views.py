# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _


from posts.forms import BlogPostForm
from posts.models import BlogPost, Album, Link, Post

from blogs.models import Blog

from notifications.forms import InvitationForm
from notifications.models import Invitation

def index(request):
      if request.META['HTTP_HOST'] == "blobon.com":
        if request.user.is_authenticated():
          blogs = Blog.objects.filter(creator=request.user)
          return render_to_response('dashboard.html',
                                    {'blogs': blogs},
                                    context_instance=RequestContext(request))
        else:
          if request.method == 'POST':
              form = InvitationForm(request.POST)
              if form.is_valid():
                  invitation = form.save()
                  messages.add_message(request, messages.INFO, _(u'Thank you for your interest in the project. %s has been added to our queue and we will contact you as soon as we can' % invitation.email))
          else:
              form = InvitationForm()
          return render_to_response('blobon.html',
                                    {'form': form},
                                     context_instance=RequestContext(request))
      elif Blog.objects.filter(custom_domain=request.META['HTTP_HOST']).exists():
          blog = Blog.objects.get(custom_domain=request.META['HTTP_HOST'])
          posts = paginate(request,
                         Post.objects.filter(blog=blog).order_by('-pub_date'),
                         15)
          return render_to_response('index.html',
                                    {'posts': posts, },
                                    context_instance=RequestContext(request))
      else:
        user = ""
        posts = paginate(request,
                         Post.objects.order_by('-pub_date'),
                         15)
        #posts= attach_infos(posts)
        #latest_comments = Comment.objects.all().order_by('-created')[:5]
        #cats = Cat.objects.filter(is_top_level=True)
        return render_to_response('index.html',
                                 {'user': user,
                                  'posts': posts, },
                                  context_instance=RequestContext(request))

def pics(request):
      posts = paginate(request,
                       Post.objects.order_by('-pub_date'),
                       15)
      return render_to_response('index.html',
                               {'posts': posts, },
                                context_instance=RequestContext(request))

def videos(request):
      posts = paginate(request,
                       Post.objects.filter(youtube_id!="").order_by('-pub_date'),
                       15)
      return render_to_response('index.html',
                               {'posts': posts},
                                context_instance=RequestContext(request))

def single(request):
        return render_to_response('single.html',
                                  {},
                                  context_instance=RequestContext(request))


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

###UTILS###
#Une fonction pour paginer une liste d'objets
def paginate(request, list_of_objects, number_of_items):
    paginator = Paginator(list_of_objects, number_of_items)
    page = request.GET.get('page')
    try:
      paginated_objects = paginator.page(page)
    except PageNotAnInteger:
      paginated_objects = paginator.page(1)
    except EmptyPage:
      paginated_objects = paginator.page(paginator.num_pages)
    return paginated_objects
