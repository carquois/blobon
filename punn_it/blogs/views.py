# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _

from blogs.forms import BlogForm
from blogs.models import Blog, Page, Tag, Category, Post

from notifications.forms import InvitationForm
from notifications.models import Invitation

def index(request):
      request.subdomain = None
      host = request.META.get('HTTP_HOST', '')
      host_s = host.replace('www.', '').split('.')
      if len(host_s) > 2:
          request.subdomain = host_s[0]
      if host == "blobon.com":
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
      elif Blog.objects.filter(custom_domain=host).exists():
          blog = Blog.objects.get(custom_domain=host)
          posts = paginate(request,
                           Post.objects.filter(blog=blog).order_by('-pub_date'),
                           15)
          return render_to_response('index.html',
                                    {'posts': posts, },
                                    context_instance=RequestContext(request))
      elif Blog.objects.filter(slug=request.subdomain).exists():
          blog = Blog.objects.get(slug=request.subdomain)
          if blog.custom_domain:
            return HttpResponseRedirect("http://%s/" % blog.custom_domain)
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
def newpost(request):
      if request.FILES.get('id_image', False):
        messages.add_message(request, messages.INFO, _(u"single image"))
      elif request.FILES.get('id_album_1_image_1', False) and request.FILES.get('id_album_1_image_2', False):
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
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')[:5]
      pages = Page.objects.filter(blog=blog)[:5]
      categories = Category.objects.filter(blog=blog)
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, 'pages': pages , 'categories': categories},
                                context_instance=RequestContext(request))

@login_required
def administrateposts(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

@login_required
def administratepages(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

@login_required
def administratecomments(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

@login_required
def administratecategories(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

@login_required
def administratetags(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

@login_required
def administratesettings(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

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
