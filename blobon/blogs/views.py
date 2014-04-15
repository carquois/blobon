# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.files.temp import NamedTemporaryFile
import urllib2
from urlparse import urlparse
from django.core.files import File
from cgi import parse_qs

from blogs.forms import BlogForm, SettingsForm, PostForm, CategoriesForm, SubscriptionForm, EmailForm, ContactForm, PasswordForm, CommentForm, PageForm, RssForm, TagsForm
from blogs.models import Blog, Page, Tag, Category, Post, Comment, Subscription, Info_email, Rss, Menu, MenuItem
from django.contrib.auth.models import User

from notifications.forms import InvitationForm
from notifications.models import Invitation

from django.forms import ModelForm, Textarea, TextInput, CharField, URLField, EmailField
from django.forms.models import modelformset_factory

from django.core.mail import send_mail
from django.views.decorators.cache import never_cache


@never_cache
def index(request):
      request.subdomain = None
      host = request.META.get('HTTP_HOST', '')
      host_s = host.replace('www.', '').split('.')
      if len(host_s) > 2:
          request.subdomain = host_s[0]
      if host == "blobon.com":
        if request.user.is_authenticated():
          return render_to_response('blogs/read.html',
                                    {},
                                    context_instance=RequestContext(request))
        else:
          if request.method == 'POST':
              form = InvitationForm(request.POST)
              if form.is_valid():
                  invitation = form.save()
                  messages.add_message(request, messages.INFO, _(u'Thank you for your interest in the project. %s has been added to our queue and we will contact you as soon as we can' % invitation.email))
          else:
              form = InvitationForm()
          return render_to_response('blogs/blobon.html',
                                    {'form': form, },
                                     context_instance=RequestContext(request))
      elif host == "gabrieldancause.com":
        return render_to_response('blogs/gabrieldancause.html',
                                  {},
                                   context_instance=RequestContext(request))
      elif host == "www.checkdonc.ca":
        return HttpResponseRedirect("http://checkdonc.ca")
      elif Blog.objects.filter(custom_domain=host).exists():
          blog = Blog.objects.get(custom_domain=host)
          menus = Menu.objects.filter(blog=blog)
          if blog.is_online == False:
            return render_to_response('blogs/closed.html',context_instance=RequestContext(request))
	  if blog.is_open == False:
            if 'is_legit' in request.session:
              b = request.session['blog']
              if b != blog:
                form = PasswordForm()
                return render_to_response('blogs/password.html',
                                          {'form': form,'blog': blog,},
                                          context_instance=RequestContext(request))
              else:
                posts = paginate(request,
                                 Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                                 6)
                form = SubscriptionForm()
                categories = Category.objects.filter(blog=blog)
                if blog.is_bootblog == True:
                  return render_to_response('blogs/blog.html',
                                            {'menus': menus, 'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                            context_instance=RequestContext(request))
                elif blog.template:
                  template = blog.template
                  return render_to_response('blogs/template_blog.html',
                                            {'posts': posts, 'blog': blog, 'form': form,'categories': categories,'template' : template,},
                                            context_instance=RequestContext(request))
                else:
                  return render_to_response('blogs/index.html',
                                            {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                            context_instance=RequestContext(request))

            else:
              form = PasswordForm()
              return render_to_response('blogs/password.html',
                                        {'form': form,'blog': blog,},
                                        context_instance=RequestContext(request))
          else: 
            posts = paginate(request,
                             Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                             6)
            form = SubscriptionForm()
            categories = Category.objects.filter(blog=blog)
            if blog.is_bootblog == True:
              return render_to_response('blogs/blog.html',
                                        {'menus': menus, 'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                        context_instance=RequestContext(request))
            elif blog.template:
              template = blog.template
              return render_to_response('blogs/template_blog.html',
                                        {'posts': posts, 'blog': blog, 'form': form,'categories': categories,'template' : template,},
                                        context_instance=RequestContext(request))
            else:
              return render_to_response('blogs/index.html',
                                        {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                        context_instance=RequestContext(request))

      elif Blog.objects.filter(slug=request.subdomain).exists():
          blog = Blog.objects.get(slug=request.subdomain)
          menus = Menu.objects.filter(blog=blog)
          if blog.is_online == False:
           return render_to_response('blogs/closed.html',context_instance=RequestContext(request))
          if blog.is_open == False:
            if 'is_legit' in request.session:
              b = request.session['blog']
              if b != blog:
                form = PasswordForm()
                return render_to_response('blogs/password.html',
                                          {'form': form,'blog': blog,},
                                          context_instance=RequestContext(request))
              else:
                if blog.custom_domain:
                  return HttpResponseRedirect("http://%s/" % blog.custom_domain)
                posts = paginate(request,
                               Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                               6)
                form = SubscriptionForm()
                categories = Category.objects.filter(blog=blog)
                if blog.is_bootblog == True:
                  return render_to_response('blogs/blog.html',
                                            {'menus': menus, 'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                            context_instance=RequestContext(request)) 
                elif blog.template:
                  template = blog.template
                  return render_to_response('blogs/template_blog.html',
                                            {'posts': posts, 'blog': blog, 'form': form,'categories': categories,'template' : template,},
                                            context_instance=RequestContext(request))
                else:
                  return render_to_response('blogs/index.html',
                                            {'posts': posts, 'blog': blog, 'form': form, 'categories': categories,},
                                            context_instance=RequestContext(request))
            else:
              form = PasswordForm()
              return render_to_response('blogs/password.html',
                                        {'form': form,'blog': blog,},
                                        context_instance=RequestContext(request))
          else:
            if blog.custom_domain:
              return HttpResponseRedirect("http://%s/" % blog.custom_domain)
            posts = paginate(request,
                           Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                           6)
            form = SubscriptionForm()
            categories = Category.objects.filter(blog=blog)
            if blog.is_bootblog == True:
              return render_to_response('blogs/blog.html',
                                        {'menus': menus, 'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                        context_instance=RequestContext(request))
            elif blog.template:
              template = blog.template
              return render_to_response('blogs/template_blog.html',
                                        {'posts': posts, 'blog': blog, 'form': form,'categories': categories,'template' : template,},
                                        context_instance=RequestContext(request))
            else:
              return render_to_response('blogs/index.html',
                                        {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                        context_instance=RequestContext(request))

      else:
        return render_to_response('404.html',
                                 {},
                                  context_instance=RequestContext(request))


def category(request, slug):
      category = get_object_or_404(Category, slug=slug)
      posts = paginate(request,
                       Post.objects.filter(status='P').filter(category=category).filter(is_discarded=False).order_by('-pub_date'),
                       6)
      blog = category.blog
      form = SubscriptionForm()
      cat = category
      categories = Category.objects.filter(blog=blog)
      menus = Menu.objects.filter(blog=blog)
      if blog.is_bootblog == True:
        return render_to_response('blogs/blog_category.html',
                                  {'menus': menus, 'cat': cat,'form': form, 'blog': blog,'posts': posts, 'category': category, 'categories': categories,},
                                  context_instance=RequestContext(request))        
      else:
        return render_to_response('blogs/category.html',
                                  {'form': form, 'blog': blog,'posts': posts, 'category': category,},
                                  context_instance=RequestContext(request))


def page(request, slug):
      page = get_object_or_404(Page, slug=slug)
      blog = page.blog
      menus = Menu.objects.filter(blog=blog)
      return render_to_response('blogs/page.html',
                                {'page': page, 'blog': blog, 'menus': menus,},
                                context_instance=RequestContext(request))




@login_required
def rss_auto_post(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      rsss = Rss.objects.filter(blog=blog).order_by('-id')
      form = RssForm()
      return render_to_response('blogs/rss_auto_post.html',
                                {'rsss': rsss, 'blog': blog, 'form': form,},
                                context_instance=RequestContext(request))
@login_required
def administrateemails(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      info_emails = Info_email.objects.filter(blog=blog).order_by('-id')
      subscriptions = Subscription.objects.filter(blog=blog).order_by('-email')
      form = EmailForm()
      subs_form = SubscriptionForm()
      return render_to_response('blogs/administrateemails.html',
                                {'subs_form': subs_form, 'blog': blog, 'info_emails': info_emails, 'form': form,'subscriptions': subscriptions,},
                                context_instance=RequestContext(request))


 
@login_required
def dashboard(request):
      blogs = Blog.objects.filter(creator=request.user,is_online=True)
      return render_to_response('blogs/dashboard.html',
                                {'blogs': blogs,},
                                context_instance=RequestContext(request))

def pics(request):
      posts = paginate(request,
                       Post.objects.order_by('-pub_date'),
                       15)
      return render_to_response('blogs/index.html',
                               {'posts': posts, },
                                context_instance=RequestContext(request))

def videos(request):
      posts = paginate(request,
                       Post.objects.filter(youtube_id != "").order_by('-pub_date'),
                       15)
      return render_to_response('blogs/index.html',
                               {'posts': posts},
                                context_instance=RequestContext(request))


@never_cache
def single(request, shorturl):
    request.subdomain = None
    host = request.META.get('HTTP_HOST', '')
    host_s = host.replace('www.', '').split('.')
    subd = host_s[0]    
    post = get_object_or_404(Post, base62id=shorturl)
    blog = post.blog
    menus = Menu.objects.filter(blog=blog)
    slug = blog.slug
    comments = Comment.objects.filter(post=post).filter(comment_status='pu').order_by('-id')
    categories = Category.objects.filter(blog=blog)
    if host == blog.custom_domain:
#    if post.blog.custom_domain:
#      home = post.blog.custom_domain
#    else:
#      home = "http://blobon.com"
      latest_post_list = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:6]
      next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]
      prev_post = ""
      next_post = ""
      form = SubscriptionForm()
      if blog.is_online == False:
        return render_to_response('blogs/closed.html',context_instance=RequestContext(request))
      if blog.is_open == False:
        if 'is_legit' in request.session:
          b = request.session['blog']
          if b != blog:
            form = PasswordForm()
            return render_to_response('blogs/passwordsingle.html',
                                      {'form': form,'blog': blog,'post': post,},
                                      context_instance=RequestContext(request))
          else:
            if Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]:
              next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:1]
              if (next_post_query.count() > 0):
                next_post = next_post_query[0]
            if Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).order_by('pub_date').exclude(pk=post.id)[:1]:
              prev_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).filter(is_top=True).filter(status='P').order_by('pub_date').exclude(pk=post.id)[:1]
              if (prev_post_query.count() > 0):
                prev_post = prev_post_query[0]

            if request.user.is_authenticated():
              comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
              if blog.is_bootblog == False and not blog.template:
                return render_to_response('blogs/single.html',
                                         {'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              elif blog.template:
                template = blog.template
                return render_to_response('blogs/template_single.html',
                                         {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,'template': template,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                return render_to_response('blogs/blog_single.html',
                                         {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
            else:
              comment_form = CommentForm()
              if blog.is_bootblog == False and not blog.template:
                return render_to_response('blogs/single.html',
                                          {'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                           'next_post': next_post, 'prev_post': prev_post,
                                           'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                           context_instance=RequestContext(request))
              elif blog.template:
                template = blog.template
                return render_to_response('blogs/template_single.html',
                                         {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,'template': template,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                return render_to_response('blogs/blog_single.html',
                                         {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
        else:
          form = PasswordForm()
          return render_to_response('blogs/passwordsingle.html',
                                    {'form': form,'blog': blog,'post': post,},
                                    context_instance=RequestContext(request))
      else:
        if Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]:
          next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:1]
          if (next_post_query.count() > 0):
            next_post = next_post_query[0]
        if Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).order_by('pub_date').exclude(pk=post.id)[:1]:
          prev_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).filter(is_top=True).filter(status='P').order_by('pub_date').exclude(pk=post.id)[:1]
          if (prev_post_query.count() > 0):
            prev_post = prev_post_query[0]
#      url = request.build_absolute_uri()


        if request.user.is_authenticated():
          comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
        else:
           comment_form = CommentForm()
        if blog.is_bootblog == False and not blog.template:
          return render_to_response('blogs/single.html',
                                    {'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                    'next_post': next_post, 'prev_post': prev_post, 
                                    'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                    context_instance=RequestContext(request))
        elif blog.template:
          template = blog.template
          return render_to_response('blogs/template_single.html',
                                   {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                   'next_post': next_post, 'prev_post': prev_post,'template': template,
                                   'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                   context_instance=RequestContext(request))
        else:
          return render_to_response('blogs/blog_single.html',
                                    {'menus': menus, 'categories': categories, 'subd': subd, 'slug': slug, 'post': post, 'latest_post_list': latest_post_list,
                                    'next_post': next_post, 'prev_post': prev_post,
                                    'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                    context_instance=RequestContext(request))                           
    elif subd == blog.slug:
      latest_post_list = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:6]
      next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]
      prev_post = ""
      next_post = ""
      form = SubscriptionForm()
      if blog.is_online == False:
        return render_to_response('blogs/closed.html',context_instance=RequestContext(request))
      if blog.is_open == False:
        if 'is_legit' in request.session:
          b = request.session['blog']
          if b != blog:
            form = PasswordForm()
            return render_to_response('blogs/passwordsingle.html',
                                      {'form': form,'blog': blog,'post': post,},
                                      context_instance=RequestContext(request))
          else:
            if Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]:
              next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:1]
              if (next_post_query.count() > 0):
                next_post = next_post_query[0]
            if Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).order_by('pub_date').exclude(pk=post.id)[:1]:
              prev_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).filter(is_top=True).filter(status='P').order_by('pub_date').exclude(pk=post.id)[:1]
              if (prev_post_query.count() > 0):
                prev_post = prev_post_query[0]


            if request.user.is_authenticated():
              comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
              if blog.is_bootblog == False and not blog.template:
                return render_to_response('blogs/single.html',
                                         {'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              elif blog.template:
                template = blog.template
                return render_to_response('blogs/template_single.html',
                                         {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,'template': template,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                return render_to_response('blogs/blog_single.html',
                                         {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
            else:
              comment_form = CommentForm()
              if blog.is_bootblog == False and not blog.template:
                return render_to_response('blogs/single.html',
                                          {'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                           'next_post': next_post, 'prev_post': prev_post,
                                           'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                           context_instance=RequestContext(request))
              elif blog.template:
                template = blog.template
                return render_to_response('blogs/template_single.html',
                                         {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,'template': template,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                return render_to_response('blogs/blog_single.html',
                                         {'menus': menus, 'categories': categories, 'subd': subd, 'slug': slug,'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))

        else:
          form = PasswordForm()
          return render_to_response('blogs/passwordsingle.html',
                                    {'form': form,'blog': blog,'post': post,},
                                    context_instance=RequestContext(request))
      else:
        if Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]:
          next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:1]
          if (next_post_query.count() > 0):
            next_post = next_post_query[0]
        if Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).order_by('pub_date').exclude(pk=post.id)[:1]:
          prev_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__gt=post.pub_date).filter(is_top=True).filter(status='P').order_by('pub_date').exclude(pk=post.id)[:1]
          if (prev_post_query.count() > 0):
            prev_post = prev_post_query[0]
#      url = request.build_absolute_uri()


        if request.user.is_authenticated():
          comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
        else:
          comment_form = CommentForm()
        if blog.is_bootblog == False and not blog.template:
          return render_to_response('blogs/single.html',
                                    {'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                    'next_post': next_post, 'prev_post': prev_post,
                                    'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                    context_instance=RequestContext(request))
        elif blog.template:
          template = blog.template
          return render_to_response('blogs/template_single.html',
                                   {'menus': menus, 'categories': categories, 'post': post, 'latest_post_list': latest_post_list,
                                   'next_post': next_post, 'prev_post': prev_post,'template': template,
                                   'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                   context_instance=RequestContext(request))
        else:
          return render_to_response('blogs/blog_single.html',
                                    {'menus': menus, 'categories': categories, 'subd': subd, 'slug': slug, 'post': post, 'latest_post_list': latest_post_list,
                                    'next_post': next_post, 'prev_post': prev_post,
                                    'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                    context_instance=RequestContext(request))

    else:
      if blog.custom_domain:
        return HttpResponseRedirect("http://" + blog.custom_domain + "/p/" + post.base62id) 
      else:
        return HttpResponseRedirect("http://" + blog.slug + ".blobon.com/p/" + post.base62id)






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
    #content = ""
    if post.content:
        post.content = linkify(punn.content)
        post.content = markdown.markdown(content)

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


@login_required
def newpost(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      form = PostForm(request.POST or None, request.FILES or None, blog=blog)
      if request.method == 'POST':
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.blog = blog
          if post.youtube_url:
            query = urlparse(post.youtube_url)
            p = parse_qs(query.query)
            post.youtube_id = p['v'][0]
          post.save()
          form.save_m2m()
          return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
        else:
          messages.add_message(request, messages.INFO, _(u"Error! Please post a valide youtube url.")) 
          return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
      return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
@login_required
def savedraft(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      form = PostForm(request.POST or None, request.FILES or None)
      if request.method == 'POST':
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.blog = blog
          post.is_ready = True
          post.status = "D"
          post.save()
          form.save_m2m()
          return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
        else:
          messages.add_message(request, messages.INFO, _(u"Error! Please post a valide youtube url."))         
          return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
      return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))

@login_required
def newcategory(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      form = CategoriesForm(request.POST or None)
      if request.method == 'POST':
        if form.is_valid():
          category = form.save(commit=False)
          category.author = request.user
          category.blog = blog
          category.save()
          return HttpResponseRedirect(reverse('blogs.views.administratecategories', args=(blog.slug,)))
      return HttpResponseRedirect(reverse('blogs.views.administratecategories', args=(blog.slug,)))


@login_required
def newrss(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      form = RssForm(request.POST or None)
      if request.method == 'POST':
        if form.is_valid():
          rss = form.save(commit=False)
          rss.blog = blog
          rss.save()
          messages.add_message(request, messages.INFO, _(u"The feed has been added"))
          return HttpResponseRedirect(reverse('blogs.views.rss_auto_post', args=(blog.slug,)))
      return HttpResponseRedirect(reverse('blogs.views.rss_auto_post', args=(blog.slug,)))

def draft(request):
      posts = paginate(request,
                       Post.objects.filter(status='D').filter(is_discarded=False).filter(is_ready=True).order_by('-pub_date'),
                       20)
      return render_to_response('blogs/index.html',
                               {'posts': posts},
                                context_instance=RequestContext(request))


@login_required
def createalbum(request):
      post = request.POST
      return render_to_response('blogs/dashboard.html',
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
            blog.is_open = False
            blog.password = request.POST['propassword']
          else:
            blog.is_open = True
          blog.save()
#          cat1 = "_Music"
#          cat2 = "_Fashion"
#          cat3 = "_Travel"
#          cat4 = "_Design"
#          cat5 = "_Food"
#          cat6 = "_Movie"
#          category, created = Category.objects.get_or_create(author=request.user, blog=blog, name="Music", slug= cat1, color="#CC0000")
#          category, created = Category.objects.get_or_create(author=request.user, blog=blog, name="Fashion", slug= cat2, color="#CC0066")
#          category, created = Category.objects.get_or_create(author=request.user, blog=blog, name="Travel", slug= cat3, color="#009900")
#          category, created = Category.objects.get_or_create(author=request.user, blog=blog, name="Design", slug= cat4, color="#669999")
#          category, created = Category.objects.get_or_create(author=request.user, blog=blog, name="Food", slug= cat5, color="#4c660f")
#          category, created = Category.objects.get_or_create(author=request.user, blog=blog, name="Movie", slug= cat6, color="#0033CC")
          messages.add_message(request, messages.INFO, _(u"Congratulation, you just created a blog"))
          return HttpResponseRedirect(reverse('blogs.views.administrateblog', args=(blog.slug,)))
      else:
        form = BlogForm()
      return render_to_response('blogs/createblog.html',
                                {'form': form},
                                context_instance=RequestContext(request))

@login_required
def administrateblog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:    
      posts = paginate(request,
                       Post.objects.filter(blog=blog).filter(is_discarded=False).order_by('-pub_date'),
                       1)
      pages = paginate(request,
                       Page.objects.order_by('-pub_date'),
                       1)
      comments = paginate(request,
                       Comment.objects.filter(blog=blog).filter(comment_status='pe').order_by('-id'),
                       1)
      info_emails = Info_email.objects.filter(blog=blog).order_by('-id')
      last_subscriber = paginate(request,
                       Subscription.objects.filter(blog=blog).order_by('-id'),
                       1)
      subscribers = paginate(request,
                       Subscription.objects.filter(blog=blog).order_by('-id'),
                       1)
      posts_to_translate = paginate(request,
                           Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('-pub_date'),
                           1)
      last_posts_to_translate = paginate(request,
                                Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('-pub_date'),
                                5)
      categories = Category.objects.filter(blog=blog).order_by('-id')
      tags = Tag.objects.filter(blog=blog).order_by('-id')
      post_form = PostForm(blog=blog)
      return render_to_response('blogs/administrateblog.html',
                                {'blog': blog,'info_emails':info_emails, 'posts_to_translate': posts_to_translate, 'last_posts_to_translate': last_posts_to_translate,'subscribers': subscribers, 'last_subscriber': last_subscriber, 'posts': posts, 'pages': pages , 'comments': comments , 'categories': categories, 'tags': tags, 'post_form': post_form},
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))
    
@login_required
def administrateposts(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      posts = Post.objects.filter(blog=blog).filter(is_discarded=False).order_by('-pub_date')
      posts = paginate(request,
                       Post.objects.filter(blog=blog).filter(is_discarded=False).order_by('-pub_date'),
                       15)
      return render_to_response('blogs/administrateposts.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def queue(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      posts = paginate(request,
                       Post.objects.filter(blog=blog).filter(is_ready=True).filter(status="D").filter(is_discarded=False).order_by('-pub_date'),
                       20)
      return render_to_response('blogs/queue.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def published(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      posts = paginate(request,
                       Post.objects.filter(blog=blog).filter(is_ready=True).filter(status="P").filter(is_discarded=False).order_by('-pub_date'),
                       20)
      return render_to_response('blogs/published.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))
@login_required
def administratepages(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      pages = Page.objects.filter(blog=blog).order_by('-pub_date')
      pages = paginate(request,
                       Page.objects.filter(blog=blog).order_by('-pub_date'),
                       15)
      return render_to_response('blogs/administratepages.html',
                                {'blog': blog, 'pages': pages, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def administratecomments(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      comments = paginate(request,
                          Comment.objects.filter(blog=blog).filter(comment_status='pe').order_by('-id'),
                          15)
      return render_to_response('blogs/administratecomments.html',
                                {'blog': blog, 'comments': comments, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def publishedcomments(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      comments = paginate(request,
                          Comment.objects.filter(blog=blog).filter(comment_status='pu').order_by('-id'),
                          15)
      return render_to_response('blogs/publishedcomments.html',
                                {'blog': blog, 'comments' : comments, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def administratecategories(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      categories = Category.objects.filter(blog=blog).order_by('-id')
      categories_form = CategoriesForm(blog=blog)
      cats_no_familly = Category.objects.filter(blog=blog).exclude(parent_category__isnull=False).exclude(child_category__isnull=False).order_by('name')
      cats_c_no_p = Category.objects.filter(blog=blog).exclude(parent_category__isnull=False).exclude(child_category__isnull=True).order_by('name')
      return render_to_response('blogs/administratecategories.html',
                                {'cats_no_familly': cats_no_familly, 'cats_c_no_p': cats_c_no_p, 'blog': blog, 'categories': categories, 'categories_form': categories_form,},
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def administratetags(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = TagsForm()
    if request.user == blog.creator:
      if request.method == 'POST':
        form = TagsForm(request.POST or None,)
        if form.is_valid():
          tag = form.save(commit=False)
          tag.author = request.user
          tag.blog = blog
          tag.save()
          messages.add_message(request, messages.INFO, _(u"The tag has been created"))
          return HttpResponseRedirect(reverse('blogs.views.administratetags', args=(blog.slug,)))
      else:
        form = TagsForm()
        tags = Tag.objects.filter(blog=blog).order_by('-id')
        return render_to_response('blogs/administratetags.html',
                                  {'blog': blog, 'tags': tags, 'form':form, },
                                  context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))


@login_required
def deletetag(request, id):
      tag = get_object_or_404(Tag, id=id)
      blog = tag.blog
      if request.user == tag.author:
        tag.delete()
        messages.add_message(request, messages.INFO, _(u"Your tag has been deleted"))
      elif request.user.is_staff:
        tag.delete()
        messages.add_message(request, messages.INFO, _(u"The tag has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.administratetags', args=(blog.slug,)))

@login_required
def edittag(request, id):
      tag = get_object_or_404(Tag, id=id)
      blog = tag.blog
      if request.method == 'POST':
        form = TagsForm(request.POST or None, instance=tag)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs.views.administratetags', args=(blog.slug,)))
      else:
        form = TagsForm(instance=tag,)
      return render_to_response('blogs/edittag.html',
                                {'blog': blog, 'form': form,'tag': tag },
                                context_instance=RequestContext(request))

@login_required
def converttag(request, id):
      tag = get_object_or_404(Tag, id=id)
      blog = tag.blog
      posts = Post.objects.filter(blog=blog).filter(tag=tag).filter(is_discarded=False).order_by('-pub_date') 
      category = Category.objects.create(name=tag.name, description=tag.description, author=tag.author, blog=blog)
      for post in posts:
        post.save()
        post.category.add(category)
        post.save()
      tag.delete()
      messages.add_message(request, messages.INFO, _(u"The tag has been change to a category"))
      return HttpResponseRedirect(reverse('blogs.views.administratecategories', args=(blog.slug,)))  


@login_required
def convertcategory(request, id):
      category = get_object_or_404(Category, id=id)
      blog = category.blog
      posts = Post.objects.filter(blog=blog).filter(category=category).filter(is_discarded=False).order_by('-pub_date')
      tag = Tag.objects.create(name=category.name, description=category.description, author=category.author, blog=blog)
      for post in posts:
        post.save()
        post.tag.add(tag)
        post.save()
      category.delete()
      messages.add_message(request, messages.INFO, _(u"The category has been change to a tag"))
      return HttpResponseRedirect(reverse('blogs.views.administratetags', args=(blog.slug,)))

@login_required
def administratesettings(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      if request.method == 'POST':
        form = SettingsForm(request.POST or None, request.FILES or None, instance=blog,)
        if form.is_valid():
            blog = form.save(commit=False)
            if blog.password:
              blog.is_open = False
            else:
              blog.is_open = True
            blog.save() 
            messages.add_message(request, messages.INFO, _(u"Your settings have been saved"))
            return HttpResponseRedirect(reverse('blogs.views.administrateblog', args=(blog.slug,)))
      else:
        form = SettingsForm(instance=blog,)
      return render_to_response('blogs/administratesettings.html',
                                {'blog': blog, 'form': form, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def administrateemails(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      info_emails = Info_email.objects.filter(blog=blog).order_by('-id')
      subscriptions = Subscription.objects.filter(blog=blog).order_by('-email')
      form = EmailForm()
      subs_form = SubscriptionForm()
      return render_to_response('blogs/administrateemails.html',
                                {'subs_form': subs_form, 'blog': blog, 'info_emails': info_emails, 'form': form,'subscriptions': subscriptions,},
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def editpost(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      categories = Category.objects.filter(blog=blog).order_by('-id')
      if request.method == 'POST':
        form = PostForm(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            if post.youtube_url:
              query = urlparse(post.youtube_url)
              p = parse_qs(query.query)
              post.youtube_id = p['v'][0]
              post.save()  
            if 'save_quit' in request.POST:
              return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
            else:
              form = PostForm(instance=post,)
              return render_to_response('blogs/editpost.html',
                                       {'blog': blog, 'form': form,'post': post,'categories': categories, },
                                       context_instance=RequestContext(request))
      else:
        form = PostForm(instance=post, blog=blog)
      return render_to_response('blogs/editpost.html',
                                {'blog': blog, 'form': form,'post': post, 'categories': categories, },
                                context_instance=RequestContext(request))


@login_required
def editpage(request, id):
      page = get_object_or_404(Page, id=id)
      blog = page.blog
      if request.method == 'POST':
        form = PageForm(request.POST or None,request.FILES or None, instance=page)
        if form.is_valid():
          form.save()
          if 'save_quit' in request.POST:
            return HttpResponseRedirect(reverse('blogs.views.administratepages', args=(blog.slug,)))
          else:
            form = PageForm(instance=page,)
            return render_to_response('blogs/editpage.html',
                                      {'blog': blog, 'form': form,'page': page, },
                                      context_instance=RequestContext(request))
      else:
        form = PageForm(instance=page)
      return render_to_response('blogs/editpage.html',
                                {'blog': blog, 'form': form,'page': page, },
                                context_instance=RequestContext(request))
@login_required
def translatepost(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      if request.method == 'POST':
        form = PostForm(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if 'save_ready_publish' in request.POST:
              post.is_ready = True
              post.status = 'P'
              post.save()
              messages.add_message(request, messages.INFO, _(u"Your post has been publish"))
              return HttpResponseRedirect(reverse('blogs.views.translation', args=(blog.slug,)))
            elif 'save_ready_queue' in request.POST:
              post.is_ready = True
              post.save()
              messages.add_message(request, messages.INFO, _(u"Your post has been add to queue"))
              return HttpResponseRedirect(reverse('blogs.views.translation', args=(blog.slug,)))
            else:
              post.save()
              messages.add_message(request, messages.INFO, _(u"Your post has been save"))
              return HttpResponseRedirect(reverse('blogs.views.translation', args=(blog.slug,)))
      else:
        form = PostForm(instance=post,)
      return render_to_response('blogs/translatepost.html',
                                {'blog': blog, 'form': form,'post': post },
                                context_instance=RequestContext(request))

@login_required
def quicktranslation(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      if request.method == 'POST':
        form = PostForm(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if not post.translated_title:
              post.is_ready = True
              post.status = 'D'
              post.is_discarded = True
              post.save()
              latest_post = Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('id')[:1]
              return HttpResponseRedirect(reverse('blogs.views.quicktranslation', args=(latest_post[0].id,)))
            else:
              post.is_ready = True
              post.status = 'D'
              post.save()
              latest_post = Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('id')[:1]
              return HttpResponseRedirect(reverse('blogs.views.quicktranslation', args=(latest_post[0].id,)))
      else:
        form = PostForm(instance=post,)
      return render_to_response('blogs/quicktranslation.html',
                                {'blog': blog, 'form': form,'post': post, },
                                context_instance=RequestContext(request))

@login_required
def translation(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user == blog.creator:
      posts = paginate(request,
                       Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('-pub_date'),
                       15)
      latest_post = Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('id')[:1]
      return render_to_response('blogs/translation.html',
                                {'blog': blog, 'posts': posts,'latest_post': latest_post, },
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def editcategory(request, id):
      category = get_object_or_404(Category, id=id)
      blog = category.blog
      if request.method == 'POST':
        form = CategoriesForm(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs.views.administratecategories', args=(blog.slug,)))
      else:
        form = CategoriesForm(instance=category,blog=blog)
      return render_to_response('blogs/editcategory.html',
                                {'blog': blog, 'form': form,'category': category },
                                context_instance=RequestContext(request))

@login_required
def editemail(request, id):
      info_email = get_object_or_404(Info_email, id=id)
      blog = info_email.blog
      if request.method == 'POST':
        form = EmailForm(request.POST or None, instance=info_email)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs.views.administrateemails', args=(blog.slug,)))
      else:
        form = EmailForm(instance=info_email,)
      return render_to_response('blogs/editemail.html',
                                {'blog': blog, 'form': form,'info_email': info_email },
                                context_instance=RequestContext(request))

@login_required
def view_info_letter(request, id):
      info_email = get_object_or_404(Info_email, id=id)
      blog = info_email.blog
      return render_to_response('blogs/view_info_letter.html',
                                {'blog': blog,'info_email': info_email },
                                context_instance=RequestContext(request))



@login_required
def fastedit(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = paginate(request,
                       Post.objects.filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('-pub_date'),
                       10)
#      PostFormset = modelformset_factory(Post, fields=('title', 'translated_title','content', 'translated_content', 'is_ready'))
#      if request.method == 'POST':
#        formset = PostFormset(request.POST or None,request.FILES or None, queryset=Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date')[:40])
#        if formset.is_valid():
#            formset.save()
#            return HttpResponseRedirect(reverse('blogs.views.administratecategories', args=(blog.slug,)))
#      else:
#        formset = PostFormset(queryset=Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date')[:40])
      return render_to_response('blogs/fastedit.html',
                                {'blog': blog, 'posts': posts},
                                context_instance=RequestContext(request))

@login_required
def fasteditpost(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      if request.method == 'POST':
        form = PostForm(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blogs.views.fastedit', args=(blog.slug,)))
#        return render_to_response('fastedit.html',
#                                  {'blog': blog, 'form': form },
#                                  context_instance=RequestContext(request))
      else:
        form = PostForm(instance=post,)
      return render_to_response('blogs/fasteditpost.html',
                                {'blog': blog, 'form': form,'post': post },
                                context_instance=RequestContext(request))

@login_required
def createpage(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      if request.method == 'POST':
        form = PageForm(request.POST or None)
        if form.is_valid():
          page = form.save(commit=False)
          page.blog = blog
          page.author = request.user
          page.save()
          messages.add_message(request, messages.INFO, _(u"Your page has been created"))
          return HttpResponseRedirect(reverse('blogs.views.administratepages', args=(blog.slug,)))
      else:
        form = PageForm() 
        return render_to_response('blogs/createpage.html',
                                  {'blog': blog, 'form': form,},
                                  context_instance=RequestContext(request))


@login_required
def submit(request): 
    from blogs.forms import SubmitForm
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
          new_post = form.save(commit=False)
          new_post.blog = request.user.userprofile.main_blog
          new_post.author = request.user
          new_post.is_ready = False
          if request.user.is_staff:
            new_post.is_top = True
            new_post.save()
          new_post.status = "D"
          new_post.save()
          new_post.source = request.POST['source']
          img_temp = NamedTemporaryFile(delete=True)
          img_temp.write(urllib2.urlopen(request.POST['media']).read())
          img_temp.flush()
          filename = urlparse(request.POST['media']).path.split('/')[-1]
          ext = filename.split('.')[-1]
          prefix = new_post.base62id
          filename = "%s.%s" % (prefix, ext)
          new_post.pic.save(filename, File(img_temp))
          if request.POST['is_video'] == 'true':
            query = urlparse(new_post.source)
            p = parse_qs(query.query)
            new_post.youtube_id = p['v'][0]
            new_post.save()
          return HttpResponseRedirect( new_post.get_absolute_url() )
    elif request.method == 'GET':
      source = request.GET.get('url', '') 
      title = request.GET.get('title', '') 
      image = request.GET.get('media', '') 
      is_video = request.GET.get('is_video', '') 
      form = SubmitForm(initial={'source':source, 'title':title, 'image': image, 'is_video':is_video})
      return render_to_response('blogs/submit.html', {'image': image, 'form': form, 'is_video': is_video}, context_instance=RequestContext(request))
    else:
      form = SubmitForm()
    return render_to_response('blogs/submit.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def deletepost(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      if request.user == post.author:
        post.delete()
        messages.add_message(request, messages.INFO, _(u"Your post has been deleted"))
      elif request.user.is_staff:
        post.delete()
        messages.add_message(request, messages.INFO, _(u"The post has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))



@login_required
def deletepost_trans(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      if request.user == post.author:
        post.is_discarded = True
        post.save()
        messages.add_message(request, messages.INFO, _(u"Your post has been deleted"))
      elif request.user.is_staff:
        post.is_discarded = True
        post.save()
        messages.add_message(request, messages.INFO, _(u"The post has been deleted"))
      latest_post = Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).filter(is_discarded=False).order_by('id')[:1]
      return HttpResponseRedirect(reverse('blogs.views.quicktranslation', args=(latest_post[0].id,)))

@login_required
def deletepage(request, id):
      page = get_object_or_404(Page, id=id)
      blog = page.blog
      if request.user == page.author:
        page.delete()
        messages.add_message(request, messages.INFO, _(u"Your page has been deleted"))
      elif request.user.is_staff:
        page.delete()
        messages.add_message(request, messages.INFO, _(u"The page has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.administratepages', args=(blog.slug,)))

@login_required
def deletecategory(request, id):
      category = get_object_or_404(Category, id=id)
      blog = category.blog
      if request.user == category.author:
        category.delete()
        messages.add_message(request, messages.INFO, _(u"Your category has been deleted"))
      elif request.user.is_staff:
        category.delete()
        messages.add_message(request, messages.INFO, _(u"The category has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.administratecategories', args=(blog.slug,)))

@login_required
def publish_now(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      post.status = 'P'
      post.save()
      messages.add_message(request, messages.INFO, _(u"The post has been publish"))
      return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))

@login_required
def publish_page_now(request, id):
      page = get_object_or_404(Page, id=id)
      blog = page.blog
      page.status = 'P'
      page.save()
      messages.add_message(request, messages.INFO, _(u"The page has been publish"))
      return HttpResponseRedirect(reverse('blogs.views.administratepages', args=(blog.slug,)))

@login_required
def deletecomment(request, id):
      comment = get_object_or_404(Comment, id=id)
      blog = comment.blog
      comment.delete()
      return HttpResponseRedirect(reverse('blogs.views.administratecomments', args=(blog.slug,)))

@login_required
def delete_pending_comments(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      comments = Comment.objects.filter(blog=blog).filter(comment_status='pe').order_by('-id')
      for comment in comments:
        comment.delete()
      return HttpResponseRedirect(reverse('blogs.views.administratecomments', args=(blog.slug,)))

@login_required
def deletecomment_from_single(request, id):
      comment = get_object_or_404(Comment, id=id)
      post = comment.post
      comment.delete()
      return HttpResponseRedirect(reverse('blogs.views.single', args=(post.base62id,)))

@login_required
def deletesubscription(request, id):
      subscription = get_object_or_404(Subscription, id=id)
      blog = subscription.blog
      subscription.delete()
      messages.add_message(request, messages.INFO, _(u"The subscriber has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.administrateemails', args=(blog.slug,)))


@login_required
def deleterss(request, id):
      rss = get_object_or_404(Rss, id=id)
      blog = rss.blog
      rss.delete()
      messages.add_message(request, messages.INFO, _(u"The feed has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.rss_auto_post', args=(blog.slug,)))


@login_required
def deleteblog(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      if request.user == blog.creator:
        blog.is_online=False
        blog.save()
        messages.add_message(request, messages.INFO, _(u"Your blog has been deleted"))
      elif request.user.is_staff:
        blog.is_online=False
        blog.save()
        messages.add_message(request, messages.INFO, _(u"The blog has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.index'))

@login_required
def approvecomment(request, id):
      comment = get_object_or_404(Comment, id=id)
      blog = comment.blog
      if request.user == blog.creator:
        comment.comment_status = "pu"
        comment.save()
      elif request.user.is_staff:
        comment.comment_status = "pu"
        comment.save()      
      return HttpResponseRedirect(reverse('blogs.views.administratecomments', args=(blog.slug,)))

@login_required
def signalcomment(request, id):
      comment = get_object_or_404(Comment, id=id)
      blog = comment.blog
      comment.comment_status = "sp"
      comment.save()
      from django.core.mail import EmailMultiAlternatives
      from django.template.loader import get_template
      from django.template import Context
      plaintext = get_template('signalemail.txt')
      htmly     = get_template('blogs/signalemail.html')

      d = Context({ 'comment_id': comment.id, 'blog': blog.title, 'slug': blog.slug , 'comment': comment, 'post': comment.post, 'name': comment.name, 'email': comment.email, 'website': comment.website, })

      subject = 'Somebody signal a spam comment on blobon.com'
      from_email = 'info@blobon.com'
      to = 'vince@blobon.com'
      text_content = plaintext.render(d)
      html_content = htmly.render(d)
      msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
      msg.attach_alternative(html_content, "text/html")
      msg.send()
      return HttpResponseRedirect(reverse('blogs.views.administratecomments', args=(blog.slug,)))

@login_required
def deleteemail(request, id):
      info_email = get_object_or_404(Info_email, id=id)
      blog = info_email.blog
      if request.user == info_email.author:
        info_email.delete()
        messages.add_message(request, messages.INFO, _(u"Your email has been deleted"))
      elif request.user.is_staff:
        info_email.delete()
        messages.add_message(request, messages.INFO, _(u"The email has been deleted"))
      return HttpResponseRedirect(reverse('blogs.views.administrateemails', args=(blog.slug,)))

def subscribe_to_infoletter(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      form = SubscriptionForm(request.POST or None, request.FILES or None)
      if request.method == 'POST':
        if form.is_valid():
          subscription = form.save(commit=False)
          subscription.blog = blog
          subscription.save()
          if 'subs_admin' in request.POST:
            messages.add_message(request, messages.INFO, _(u"A new subscriber has been added to your blog"))
            return HttpResponseRedirect(reverse('blogs.views.administrateemails', args=(blog.slug,)))
          else:
            return render_to_response('blogs/thanks.html', {'blog': blog,}, context_instance=RequestContext(request))
      return render_to_response('blogs/subscription.html', {'form': form, 'blog': blog,}, context_instance=RequestContext(request))

@login_required
def create_info_email(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      form = EmailForm(request.POST or None, request.FILES or None)
      if request.method == 'POST':
        if form.is_valid():            
          email = form.save(commit=False)
          email.author = request.user
          email.blog = blog
          email.status = "D"
          email.save()
          return HttpResponseRedirect(reverse('blogs.views.administrateemails', args=(blog.slug,)))
      return render_to_response('blogs/administrateblog.html', {'form': form})

@login_required
def send_email_now(request, id):
      info_email = get_object_or_404(Info_email, id=id)
      blog = info_email.blog
      subject = info_email.subject
      text_content = info_email.message
#Va falloir qu'un blog aille un mail (ou user... à voir)
      from_email = 'vincegothier@gmail.com'
      recipient_list = []
      if info_email.subscribers == 'A':
        for subscription in Subscription.objects.filter(blog=blog):
          recipient_list.append(subscription.email)
          subscription.is_new = False
          subscription.save()
        from django.core.mail import EmailMultiAlternatives
        msg = EmailMultiAlternatives(subject, text_content, from_email, bcc=recipient_list)
        msg.send()
        messages.add_message(request, messages.INFO, _(u"Your message has been sent, thank you!"))
        return HttpResponseRedirect(reverse('blogs.views.administrateemails', args=(blog.slug,)))
      else:
        for subscription in Subscription.objects.filter(blog=blog).filter(is_new=True):
          recipient_list.append(subscription.email)
          subscription.is_new = False
          subscription.save()
        from django.core.mail import EmailMultiAlternatives
        msg = EmailMultiAlternatives(subject, text_content, from_email, bcc=recipient_list)
        msg.send()
        messages.add_message(request, messages.INFO, _(u"Your message has been sent, thank you!"))
        return HttpResponseRedirect(reverse('blogs.views.administrateemails', args=(blog.slug,)))

def password(request, slug):
     blog = get_object_or_404(Blog, slug=slug)
     if request.method == 'POST':
       form = PasswordForm(request.POST or None,)
       if form.is_valid():
         pw = blog.password
         password = form.cleaned_data['password']
         if password == pw:
           request.session.set_expiry(14400)
           request.session['is_legit'] = 'True'
           request.session['blog'] = blog
           return HttpResponseRedirect(reverse('blogs.views.index'))
         else:
           messages.add_message(request, messages.INFO, _(u"The password didn't match. Please try again."))
           return render_to_response('blogs/password.html',
                                     {'form': form,'blog': blog,},
                                      context_instance=RequestContext(request))
       else:
         form = PasswordForm()
         return render_to_response('blogs/password.html',
                                   {'form': form,'blog': blog,},
                                   context_instance=RequestContext(request))
     else:
       form = PasswordForm()
       return render_to_response('blogs/password.html',
                                 {'form': form,'blog': blog,},
                                 context_instance=RequestContext(request))
def passwordsingle(request, id):
     post = get_object_or_404(Post, id=id)
     blog = post.blog
     latest_post_list = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:6]
     next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]
     prev_post = ""
     next_post = ""
     if request.method == 'POST':
       form = PasswordForm(request.POST or None,)
       if form.is_valid():
         pw = blog.password
         password = form.cleaned_data['password']
         if password == pw:
           request.session.set_expiry(14400)
           request.session['is_legit'] = 'True'
           request.session['blog'] = blog
           return HttpResponseRedirect(reverse('blogs.views.single', args=(post.base62id,)))
         else:
           messages.add_message(request, messages.INFO, _(u"The password didn't match. Please try again."))
           return render_to_response('blogs/passwordsingle.html',
                                     {'form': form,'blog': blog,'post': post,},
                                      context_instance=RequestContext(request))
       else:
         form = PasswordForm()
         return render_to_response('blogs/passwordsingle.html',
                                   {'form': form,'blog': blog,'post': post,},
                                   context_instance=RequestContext(request))
     else:
       form = PasswordForm()
       return render_to_response('blogs/passwordsingle.html',
                                 {'form': form,'blog': blog,'post': post,},
                                 context_instance=RequestContext(request))


def newcomment(request, id):
     post = get_object_or_404(Post, id=id)
     blog = post.blog
     secondmoderator = blog.creator
     form = CommentForm(request.POST or None,)
     if blog.moderator_email:
       mailto = blog.moderator_email
     else:
       mailto = blog.creator.email
     blog_title = blog.title
     slug = blog.slug
     if request.method == 'POST':
       if form.is_valid():
         comment = form.save(commit=False)
         comment.blog = blog
         if request.user.is_authenticated():
           author = User.objects.get(username=request.user.username)
           comment.author = author
         comment.post = post
         comment.comment_status = "pe"
         comment.save()
         if comment.occupation:
           comment.delete()
           return HttpResponseRedirect(reverse('blogs.views.single', args=(post.base62id,)))
         else:
           from django.core.mail import EmailMultiAlternatives
           from django.template.loader import get_template
           from django.template import Context
           plaintext = get_template('email.txt')
           htmly     = get_template('blogs/email.html')

           d = Context({ 'blog_title': blog_title, 'slug': slug , 'comment': comment, 'post': post, 'name': comment.name, 'email': comment.email, 'website': comment.website, })  

           subject = 'You have a new comment'
           from_email = 'info@blobon.com'
           to = mailto
           text_content = plaintext.render(d)
           html_content = htmly.render(d)
           msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
           msg.attach_alternative(html_content, "text/html")
           msg.send()
           if request.POST.get('check', True):
             subs_form = SubscriptionForm()
             subscription = subs_form.save(commit=False)
             subscription.blog = blog
             subscription.email = comment.email
#             subscription = Subscription.objects.create_subscription(blog=blog, email=comment.email)
             subscription.save()
             messages.add_message(request, messages.INFO, _(u"Thank you. Your comment is now awaiting moderation"))
           return HttpResponseRedirect(reverse('blogs.views.single', args=(post.base62id,)))
       else:
         return render_to_response('blogs/errors.html',
                                   {'form': form,'blog': blog,'post': post,},
                                   context_instance=RequestContext(request))

#     else:
#       form = PasswordForm()
#       return render_to_response('passwordsingle.html',
#                                 {'form': form,'blog': blog,'post': post,},
#                                 context_instance=RequestContext(request))


def contact(request):
     if request.method == 'POST':
      form = ContactForm(request.POST or None, request.FILES or None)
      if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
#modifier le recipients pour info@blobon.com avant de migrer
        recipients = ['info@blobon.com']
        messages.add_message(request, messages.INFO, _(u"Your message has been sent, thank you!"))
        from django.core.mail import send_mail
        send_mail(subject, message, from_email, recipients)
        return HttpResponseRedirect(reverse('blogs.views.index'))
      else:
        form=ContactForm()
        messages.add_message(request, messages.INFO, _(u"Oups! It didn't work, please try again with a valid email"))
        return render_to_response('blogs/contact.html', 
                                  {'form': form},
                                  context_instance=RequestContext(request))
     else:
       if request.user.is_authenticated(): 
         u=User.objects.get(username=request.user.username)
         form=ContactForm(initial={'from_email':u.email})
         return render_to_response('blogs/contact.html',
                                   {'form': form, 'u': u,},
                                   context_instance=RequestContext(request))
       else:
         form=ContactForm()
         return render_to_response('blogs/contact.html',
                                   {'form': form},
                                   context_instance=RequestContext(request))     
def entreprise(request):
     if request.method == 'POST':
      form = ContactForm(request.POST or None, request.FILES or None)
      if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
#modifier le recipients pour info@blobon.com avant de migrer
        recipients = ['info@blobon.com']
        messages.add_message(request, messages.INFO, _(u"Your message has been sent, thank you!"))
        from django.core.mail import send_mail
        send_mail(subject, message, from_email, recipients)
        return HttpResponseRedirect(reverse('blogs.views.entreprise'))
      else:
        form=ContactForm()
        messages.add_message(request, messages.INFO, _(u"Oups! It didn't work, please try again with a valid email"))
        return render_to_response('blogs/entreprise.html', 
                                  {'form': form},
                                  context_instance=RequestContext(request))
     else:
       form=ContactForm()
       return render_to_response('blogs/entreprise.html',
                                 {'form': form},
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
