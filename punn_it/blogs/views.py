# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _

from blogs.forms import BlogForm, SettingsForm, PostForm
from blogs.models import Blog, Page, Tag, Category, Post, Comment

from notifications.forms import InvitationForm
from notifications.models import Invitation

from django.forms import ModelForm, Textarea, TextInput, CharField, URLField

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
                                    {'form': form, },
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

def single(request, shorturl):
    post = get_object_or_404(Post, base62id=shorturl)
    #cats = Cat.objects.filter(is_top_level=True)
    #votesup = PunnVote.objects.filter(punn=punn).filter(vote='U')
    #votesdown = PunnVote.objects.filter(punn=punn).filter(vote='D')
    #karma = votesup.count() - votesdown.count()
    #auth_user = ""
    #vote = ""
    #if request.user.is_authenticated():
    #  auth_user = request.user
    #  if PunnVote.objects.filter(punn=punn).filter(user=auth_user):
    #    if PunnVote.objects.filter(punn=punn).filter(user=auth_user).filter(vote='U'):
    #      vote = 'U'
    #    else:
    #      vote = 'D'
    #if punn.author.userprofile.domain:
    #  home = punn.author.userprofile.domain
    #else:
    #  home = "http://checkdonc.ca"
    latest_post_list = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:6]
    next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]
    prev_post = ""
    next_post = ""
    if Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]:
      next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:1]
      if (next_post_query.count() > 0):
        next_post = next_post_query[0]
    if Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).order_by('pub_date').exclude(pk=post.id)[:1]:
      prev_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).filter(is_top=True).filter(status='P').order_by('pub_date').exclude(pk=post.id)[:1]
      if (prev_post_query.count() > 0):
        prev_post = prev_post_query[0]
    #content = ""
    #if punn.content:
    #    content = linkify(punn.content)
    #    content = markdown.markdown(content)

    ##save new comment before querying for comments related to this punn
    #comment_form = CommentForm(request.POST or None)
    #if request.user.is_authenticated() and comment_form.is_valid():
    #    from earnings.models import Earning
    #    from datetime import datetime
    #    from decimal import Decimal
    #    comment = comment_form.save(commit=False)
    #    comment.punn = punn
    #    comment.author = request.user
    #    comment.save()
    #    vote = CommentVote(comment=comment, user=request.user, vote='U')
    #    vote.save()
    #    e = Earning(user=request.user, amount=Decimal("0.01"), date=datetime.now())
    #    e.save()
    #    #redirect user so a refresh doesn't trigger a double post
    #    return HttpResponseRedirect( punn.get_absolute_url() )

    #comment_list = Comment.objects.filter(punn=punn).order_by('-pub_date')
    #for comment in comment_list:
    #    comment.content = linkify(comment.content)
    #    comment.content = markdown.markdown(comment.content)
    #    votesup = CommentVote.objects.filter(comment=comment).filter(vote='U')
    #    votesdown = CommentVote.objects.filter(comment=comment).filter(vote='D')
    #    comment.karma = votesup.count() - votesdown.count()

    #    if request.user.is_authenticated() and CommentVote.objects.filter(comment=comment).filter(user=request.user).exists():
    #      v = CommentVote.objects.filter(comment=comment).filter(user=request.user)
    #      if v[0].vote == "U":
    #        comment.vote = "U"
    #      elif v[0].vote == "D":
    #        comment.vote = "D"

    #if request.user.is_authenticated() and Reblog.objects.filter(origin=punn).filter(author=request.user).exists():
    #      reblog = True
    #else:
    #      reblog = False

    #if request.user.is_authenticated() and Favorite.objects.filter(punn=punn).filter(author=request.user).exists():
    #      favorite = True
    #else:
    #      favorite = False

    #url = request.build_absolute_uri()
    #site_description = settings.MAIN_SITE_DESCRIPTION
    #site = get_current_site(request)
    return render_to_response('single.html',
                              {'post': post, 'latest_post_list': latest_post_list,
                               'next_post': next_post, 'prev_post': prev_post,},
                              context_instance=RequestContext(request))


@login_required
def newpost(request):
      if request.FILES.get('id_image', False):
        messages.add_message(request, messages.INFO, _(u"single image"))
        image = request.FILES.get('id_image')
        
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
      posts = paginate(request,
                       Post.objects.filter(blog=blog).order_by('-pub_date'),
                       1)
      pages = paginate(request,
                       Page.objects.order_by('-pub_date'),
                       1)
      comments = paginate(request,
                       Comment.objects.order_by('-id'),
                       1)
      categories = Category.objects.filter(blog=blog).order_by('-id')
      tags = Tag.objects.filter(blog=blog).order_by('-id')
      post_form = PostForm()
      return render_to_response('administrateblog.html',
                                {'blog': blog, 'posts': posts, 'pages': pages , 'comments': comments , 'categories': categories, 'tags': tags, 'post_form': post_form},
                                context_instance=RequestContext(request))

@login_required
def administrateposts(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).order_by('-pub_date')
      posts = paginate(request,
                       Post.objects.filter(blog=blog).order_by('-pub_date'),
                       15)
      return render_to_response('administrateposts.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

@login_required
def administratepages(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      pages = Page.objects.filter(blog=blog).order_by('-pub_date')
      pages = paginate(request,
                       Page.objects.order_by('-pub_date'),
                       15)
      return render_to_response('administratepages.html',
                                {'blog': blog, 'pages': pages, },
                                context_instance=RequestContext(request))

@login_required
def administratecomments(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      comments = paginate(request,
                       Comment.objects.order_by('-id'),
                       15)
      return render_to_response('administratecomments.html',
                                {'blog': blog, 'comments': comments, },
                                context_instance=RequestContext(request))

@login_required
def administratecategories(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      categories = Category.objects.filter(blog=blog).order_by('-id')
      return render_to_response('administratecategories.html',
                                {'blog': blog, 'categories': categories, },
                                context_instance=RequestContext(request))

@login_required
def administratetags(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      tags = Tag.objects.filter(blog=blog).order_by('-id')
      return render_to_response('administratetags.html',
                                {'blog': blog, 'tags': tags, },
                                context_instance=RequestContext(request))

@login_required
def administratesettings(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      if request.method == 'POST':
        form = SettingsForm(request.POST, instance=blog,)
        if form.is_valid():
          blog = form.save()
        return HttpResponseRedirect(reverse('blogs.views.administratesettings', args=(blog.slug,)))
      else:
        form = SettingsForm(instance=blog,)
      return render_to_response('administratesettings.html',
                                {'blog': blog, 'form': form, },
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

@login_required
def deletepost(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      if request.user == post.author:
        post.delete()
        messages.add_message(request, messages.INFO, _(u"The post has been deleted"))
      elif request.user.is_staff:
        post.delete()
        messages.add_message(request, messages.INFO, _(u"The post has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
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
