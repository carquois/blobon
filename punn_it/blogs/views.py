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

from blogs.forms import BlogForm, SettingsForm, PostForm, CategoriesForm, SubscriptionForm, EmailForm, ContactForm, PasswordForm, CommentForm
from blogs.models import Blog, Page, Tag, Category, Post, Comment, Subscription, Info_email
from django.contrib.auth.models import User

from notifications.forms import InvitationForm
from notifications.models import Invitation

from django.forms import ModelForm, Textarea, TextInput, CharField, URLField, EmailField
from django.forms.models import modelformset_factory

from django.core.mail import send_mail

def index(request):
      request.subdomain = None
      host = request.META.get('HTTP_HOST', '')
      host_s = host.replace('www.', '').split('.')
      if len(host_s) > 2:
          request.subdomain = host_s[0]
      if host == "blobon.com":
        if request.user.is_authenticated():
          blogs = Blog.objects.filter(creator=request.user,is_online=True)
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
          if blog.is_online == False:
            return render_to_response('closed.html',context_instance=RequestContext(request))
	  if blog.is_open == False:
            if 'is_legit' in request.session:
              b = request.session['blog']
              if b != blog:
                form = PasswordForm()
                return render_to_response('password.html',
                                          {'form': form,'blog': blog,},
                                          context_instance=RequestContext(request))
              else:
                posts = paginate(request,
                                 Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                                 15)
                form = SubscriptionForm()
                categories = Category.objects.filter(blog=blog)
                if blog.has_template == False:
                  return render_to_response('index.html',
                                            {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                            context_instance=RequestContext(request))
                else:
                  return render_to_response('blog_template.html',
                                            {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                            context_instance=RequestContext(request))
            else:
              form = PasswordForm()
              return render_to_response('password.html',
                                        {'form': form,'blog': blog,},
                                        context_instance=RequestContext(request))
          else: 
            posts = paginate(request,
                             Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                             15)
            form = SubscriptionForm()
            categories = Category.objects.filter(blog=blog)
            if blog.has_template == False:
              return render_to_response('index.html',
                                        {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                        context_instance=RequestContext(request))
            else:
              return render_to_response('blog_template.html',
                                        {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                        context_instance=RequestContext(request))
      elif Blog.objects.filter(slug=request.subdomain).exists():
          blog = Blog.objects.get(slug=request.subdomain)
          if blog.is_online == False:
           return render_to_response('closed.html',context_instance=RequestContext(request))
          if blog.is_open == False:
            if 'is_legit' in request.session:
              b = request.session['blog']
              if b != blog:
                form = PasswordForm()
                return render_to_response('password.html',
                                          {'form': form,'blog': blog,},
                                          context_instance=RequestContext(request))
              else:
                if blog.custom_domain:
                  return HttpResponseRedirect("http://%s/" % blog.custom_domain)
                posts = paginate(request,
                               Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                               15)
                form = SubscriptionForm()
                categories = Category.objects.filter(blog=blog)
                if blog.has_template == False:
                  return render_to_response('index.html',
                                            {'posts': posts, 'blog': blog, 'form': form, 'categories': categories,},
                                            context_instance=RequestContext(request))
                else:
                  return render_to_response('blog_template.html',
                                            {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                            context_instance=RequestContext(request))
            else:
              form = PasswordForm()
              return render_to_response('password.html',
                                        {'form': form,'blog': blog,},
                                        context_instance=RequestContext(request))
          else:
            if blog.custom_domain:
              return HttpResponseRedirect("http://%s/" % blog.custom_domain)
            posts = paginate(request,
                           Post.objects.filter(blog=blog).filter(status='P').order_by('-pub_date'),
                           15)
            form = SubscriptionForm()
            categories = Category.objects.filter(blog=blog)
            if blog.has_template == False:
              return render_to_response('index.html',
                                        {'posts': posts, 'blog': blog, 'form': form, 'categories': categories,},
                                        context_instance=RequestContext(request))
            else:
              return render_to_response('blog_template.html',
                                        {'posts': posts, 'blog': blog, 'form': form,'categories': categories,},
                                        context_instance=RequestContext(request))
      else:
        user = ""
        posts = paginate(request,
                         Post.objects.order_by('-pub_date'),
                         15)
        form = SubscriptionForm()
        return render_to_response('index.html',
                                 {'user': user,
                                  'posts': posts,
                                  'form': form, },
                                  context_instance=RequestContext(request))


def category(request, slug):
      category = get_object_or_404(Category, slug=slug)
      posts = paginate(request,
                       Post.objects.filter(status='P').filter(category=category).order_by('-pub_date'),
                       15)
      blog = category.blog
      form = SubscriptionForm()
      return render_to_response('category.html',
                                {'form': form, 'blog': blog,'posts': posts, 'category': category,},
                                context_instance=RequestContext(request))

def testbloggab(request):
      blog = Blog.objects.get(slug='gab')
      posts = paginate(request,
                       Post.objects.filter(blog=blog).order_by('-pub_date'),
                       5)
      form = SubscriptionForm()
      return render_to_response('testbloggab.html',
                                {'posts': posts, 'blog': blog,'form': form,},
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
                       Post.objects.filter(youtube_id != "").order_by('-pub_date'),
                       15)
      return render_to_response('index.html',
                               {'posts': posts},
                                context_instance=RequestContext(request))

def single(request, shorturl):
    request.subdomain = None
    host = request.META.get('HTTP_HOST', '')
    host_s = host.replace('www.', '').split('.')
    if len(host_s) > 2:
      request.subdomain = host_s[0]    
    post = get_object_or_404(Post, base62id=shorturl)
    blog = post.blog
    comments = Comment.objects.filter(post=post).filter(comment_status='pu').order_by('-id')
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
        return render_to_response('closed.html',context_instance=RequestContext(request))
      if blog.is_open == False:
        if 'is_legit' in request.session:
          b = request.session['blog']
          if b != blog:
            form = PasswordForm()
            return render_to_response('passwordsingle.html',
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
            if blog.has_template == False:
              if request.user.is_authenticated():
                comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
                return render_to_response('single.html',
                                         {'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                comment_form = CommentForm()
                return render_to_response('single.html',
                                          {'post': post, 'latest_post_list': latest_post_list,
                                           'next_post': next_post, 'prev_post': prev_post,
                                           'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                           context_instance=RequestContext(request))
            else:
              if request.user.is_authenticated():
                comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
                return render_to_response('single.html',
                                         {'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                comment_form = CommentForm()
                return render_to_response('single_template.html',
                                          {'post': post, 'latest_post_list': latest_post_list,
                                           'next_post': next_post, 'prev_post': prev_post,
                                           'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                           context_instance=RequestContext(request))
        else:
          form = PasswordForm()
          return render_to_response('passwordsingle.html',
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
        if blog.has_template == False:
          if request.user.is_authenticated():
            comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
          else:
             comment_form = CommentForm()
          return render_to_response('single.html',
                                    {'post': post, 'latest_post_list': latest_post_list,
                                    'next_post': next_post, 'prev_post': prev_post, 
                                    'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                    context_instance=RequestContext(request))
        else:
          comment_form = CommentForm()
          return render_to_response('single_template.html',
                                    {'post': post, 'latest_post_list': latest_post_list,
                                     'next_post': next_post, 'prev_post': prev_post,
                                     'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                     context_instance=RequestContext(request))
    elif blog.slug == host:
      latest_post_list = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).filter(is_top=True).filter(status='P').order_by('-pub_date').exclude(pk=post.id)[:6]
      next_post_query = Post.objects.filter(blog=post.blog).filter(pub_date__lt=post.pub_date).order_by('-pub_date').exclude(pk=post.id)[:1]
      prev_post = ""
      next_post = ""
      form = SubscriptionForm()
      if blog.is_online == False:
        return render_to_response('closed.html',context_instance=RequestContext(request))
      if blog.is_open == False:
        if 'is_legit' in request.session:
          b = request.session['blog']
          if b != blog:
            form = PasswordForm()
            return render_to_response('passwordsingle.html',
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
            if blog.has_template == False:
              if request.user.is_authenticated():
                comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
                return render_to_response('single.html',
                                         {'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                comment_form = CommentForm()
                return render_to_response('single.html',
                                          {'post': post, 'latest_post_list': latest_post_list,
                                           'next_post': next_post, 'prev_post': prev_post,
                                           'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                           context_instance=RequestContext(request))
            else:
              if request.user.is_authenticated():
                comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
                return render_to_response('single.html',
                                         {'post': post, 'latest_post_list': latest_post_list,
                                         'next_post': next_post, 'prev_post': prev_post,
                                         'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                         context_instance=RequestContext(request))
              else:
                comment_form = CommentForm()
                return render_to_response('single_template.html',
                                          {'post': post, 'latest_post_list': latest_post_list,
                                           'next_post': next_post, 'prev_post': prev_post,
                                           'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments,},
                                           context_instance=RequestContext(request))
        else:
          form = PasswordForm()
          return render_to_response('passwordsingle.html',
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
        if blog.has_template == False:
          if request.user.is_authenticated():
            comment_form = CommentForm(initial={'email':request.user.email,'name':request.user.get_full_name,})
          else:
             comment_form = CommentForm()
          return render_to_response('single.html',
                                    {'post': post, 'latest_post_list': latest_post_list,
                                    'next_post': next_post, 'prev_post': prev_post,
                                    'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                    context_instance=RequestContext(request))
        else:
          comment_form = CommentForm()
          return render_to_response('single_template.html',
                                    {'post': post, 'latest_post_list': latest_post_list,
                                     'next_post': next_post, 'prev_post': prev_post,
                                     'user': post.author, 'blog': post.blog, 'form': form, 'comment_form': comment_form, 'comments': comments, },
                                     context_instance=RequestContext(request))
    else:
      if blog.custom_domain:
        return HttpResponseRedirect("http://" + blog.custom_domain + "/p/" + post.base62id) 
      else:
        return HttpResponseRedirect("http://" + blog.slug + "/p/" + post.base62id)






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
          post.is_ready = True
          if post.youtube_url:
            query = urlparse(post.youtube_url)
            p = parse_qs(query.query)
            post.youtube_id = p['v'][0]
          post.save()
          form.save_m2m()
          return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
      return render_to_response('administrateblog.html', {'form': form})

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
      return render_to_response('administrateblog.html', {'form': form})

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
      return render_to_response('administrateblog.html', {'form': form})

def draft(request):
      posts = paginate(request,
                       Post.objects.filter(status='D').order_by('-pub_date'),
                       20)
      return render_to_response('index.html',
                               {'posts': posts},
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
                           Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date'),
                           1)
      last_posts_to_translate = paginate(request,
                                Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date'),
                                5)
      categories = Category.objects.filter(blog=blog).order_by('-id')
      tags = Tag.objects.filter(blog=blog).order_by('-id')
      post_form = PostForm(blog=blog)
      return render_to_response('administrateblog.html',
                                {'blog': blog,'info_emails':info_emails, 'posts_to_translate': posts_to_translate, 'last_posts_to_translate': last_posts_to_translate,'subscribers': subscribers, 'last_subscriber': last_subscriber, 'posts': posts, 'pages': pages , 'comments': comments , 'categories': categories, 'tags': tags, 'post_form': post_form},
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
      comments = Comment.objects.filter(blog=blog).filter(comment_status='pe').order_by('-id')
      comments_pu = paginate(request,
                          Comment.objects.filter(blog=blog).filter(comment_status='pu').order_by('-id'),
                       15)
      pucomments = Comment.objects.filter(blog=blog).filter(comment_status='pu').order_by('-id')
      return render_to_response('administratecomments.html',
                                {'blog': blog, 'comments': comments, 'pucomments': pucomments,'comments_pu' : comments_pu, },
                                context_instance=RequestContext(request))

@login_required
def administratecategories(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      categories = Category.objects.filter(blog=blog).order_by('-id')
      categories_form = CategoriesForm()
      return render_to_response('administratecategories.html',
                                {'blog': blog, 'categories': categories, 'categories_form': categories_form},
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
        form = SettingsForm(request.POST or None, instance=blog,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs.views.administratesettings', args=(blog.slug,)))
      else:
        form = SettingsForm(instance=blog,)
      return render_to_response('administratesettings.html',
                                {'blog': blog, 'form': form, },
                                context_instance=RequestContext(request))


@login_required
def administrateemails(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      info_emails = Info_email.objects.filter(blog=blog).order_by('-id')
      subscriptions = Subscription.objects.filter(blog=blog).order_by('-email')
      form = EmailForm()
      return render_to_response('administrateemails.html',
                                {'blog': blog, 'info_emails': info_emails, 'form': form,'subscriptions': subscriptions,},
                                context_instance=RequestContext(request))

@login_required
def editpost(request, id):
      post = get_object_or_404(Post, id=id)
      blog = post.blog
      categories = Category.objects.filter(blog=blog).order_by('-id')
      if request.method == 'POST':
        form = PostForm(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            if 'save_quit' in request.POST:
              return HttpResponseRedirect(reverse('blogs.views.administrateposts', args=(blog.slug,)))
            else:
              form = PostForm(instance=post,)
              return render_to_response('editpost.html',
                                       {'blog': blog, 'form': form,'post': post,'categories': categories, },
                                       context_instance=RequestContext(request))
      else:
        form = PostForm(instance=post, blog=blog)
      return render_to_response('editpost.html',
                                {'blog': blog, 'form': form,'post': post, 'categories': categories, },
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
              return HttpResponseRedirect(reverse('blogs.views.translation', args=(blog.slug,)))
            elif 'save_ready_queue' in request.POST:
              post.is_ready = True
              post.save()
              return HttpResponseRedirect(reverse('blogs.views.translation', args=(blog.slug,)))
            else:
              post.save()
              return HttpResponseRedirect(reverse('blogs.views.translation', args=(blog.slug,)))
      else:
        form = PostForm(instance=post,)
      return render_to_response('translatepost.html',
                                {'blog': blog, 'form': form,'post': post },
                                context_instance=RequestContext(request))

@login_required
def quicktranslation(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date')[:1]
      if not posts:
        return HttpResponseRedirect(reverse('blogs.views.translation', args=(blog.slug,)))
      else:
        for post in posts:
          post.id
        if request.method == 'POST':
          form = PostForm(request.POST or None,request.FILES or None, instance=post)
          if form.is_valid():
              post = form.save(commit=False)
              if 'save_ready_publish' in request.POST:
                post.is_ready = True
                post.status = 'P'
                post.save()
                return HttpResponseRedirect(reverse('blogs.views.quicktranslation', args=(blog.slug,)))
              elif 'save_ready_queue' in request.POST:
                post.is_ready = True
                post.save()
                return HttpResponseRedirect(reverse('blogs.views.quicktranslation', args=(blog.slug,)))
              else:
                post.save()
                return HttpResponseRedirect(reverse('blogs.views.quicktranslation', args=(blog.slug,)))
        else:
          form = PostForm(instance=post,)
        return render_to_response('quicktranslation.html',
                                  {'blog': blog, 'form': form,'post': post },
                                  context_instance=RequestContext(request))

@login_required
def translation(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = paginate(request,
                       Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date'),
                       15)
      return render_to_response('translation.html',
                                {'blog': blog, 'posts': posts, },
                                context_instance=RequestContext(request))

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
        form = CategoriesForm(instance=category,)
      return render_to_response('editcategory.html',
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
      return render_to_response('editemail.html',
                                {'blog': blog, 'form': form,'info_email': info_email },
                                context_instance=RequestContext(request))

@login_required
def view_info_letter(request, id):
      info_email = get_object_or_404(Info_email, id=id)
      blog = info_email.blog
      return render_to_response('view_info_letter.html',
                                {'blog': blog,'info_email': info_email },
                                context_instance=RequestContext(request))



@login_required
def fastedit(request, slug):
      blog = get_object_or_404(Blog, slug=slug)
      posts = paginate(request,
                       Post.objects.filter(status="D").filter(is_ready=False).order_by('-pub_date'),
                       10)
#      PostFormset = modelformset_factory(Post, fields=('title', 'translated_title','content', 'translated_content', 'is_ready'))
#      if request.method == 'POST':
#        formset = PostFormset(request.POST or None,request.FILES or None, queryset=Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date')[:40])
#        if formset.is_valid():
#            formset.save()
#            return HttpResponseRedirect(reverse('blogs.views.administratecategories', args=(blog.slug,)))
#      else:
#        formset = PostFormset(queryset=Post.objects.filter(blog=blog).filter(status="D").filter(is_ready=False).order_by('-pub_date')[:40])
      return render_to_response('fastedit.html',
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
      return render_to_response('fasteditpost.html',
                                {'blog': blog, 'form': form,'post': post },
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
      return render_to_response('submit.html', {'image': image, 'form': form, 'is_video': is_video}, context_instance=RequestContext(request))
    else:
      form = SubmitForm()
    return render_to_response('submit.html', {'form': form}, context_instance=RequestContext(request))


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
def deletecomment(request, id):
      comment = get_object_or_404(Comment, id=id)
      blog = comment.blog
      comment.delete()
      return HttpResponseRedirect(reverse('blogs.views.administratecomments', args=(blog.slug,)))

@login_required
def deletecomment_from_single(request, id):
      comment = get_object_or_404(Comment, id=id)
      post = comment.post
      comment.delete()
      return HttpResponseRedirect(reverse('blogs.views.single', args=(post.base62id,)))


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
      htmly     = get_template('signalemail.html')

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
          return render_to_response('thanks.html', {'blog': blog,}, context_instance=RequestContext(request))
      return render_to_response('subscription.html', {'form': form, 'blog': blog,}, context_instance=RequestContext(request))

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
      return render_to_response('administrateblog.html', {'form': form})

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
           return render_to_response('password.html',
                                     {'form': form,'blog': blog,},
                                      context_instance=RequestContext(request))
       else:
         form = PasswordForm()
         return render_to_response('password.html',
                                   {'form': form,'blog': blog,},
                                   context_instance=RequestContext(request))
     else:
       form = PasswordForm()
       return render_to_response('password.html',
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
           return render_to_response('passwordsingle.html',
                                     {'form': form,'blog': blog,'post': post,},
                                      context_instance=RequestContext(request))
       else:
         form = PasswordForm()
         return render_to_response('passwordsingle.html',
                                   {'form': form,'blog': blog,'post': post,},
                                   context_instance=RequestContext(request))
     else:
       form = PasswordForm()
       return render_to_response('passwordsingle.html',
                                 {'form': form,'blog': blog,'post': post,},
                                 context_instance=RequestContext(request))


def newcomment(request, id):
     post = get_object_or_404(Post, id=id)
     blog = post.blog
     form = CommentForm(request.POST or None,)
     if blog.moderator_email:
       mailto = blog.moderator_email
     else:
       mailto = 'vince@blobon.com'
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
           htmly     = get_template('email.html')

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
           return HttpResponseRedirect(reverse('blogs.views.single', args=(post.base62id,)))
       else:
         return render_to_response('errors.html',
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
        return render_to_response('contact.html', 
                                  {'form': form},
                                  context_instance=RequestContext(request))
     else:
       if request.user.is_authenticated(): 
         u=User.objects.get(username=request.user.username)
         form=ContactForm(initial={'from_email':u.email})
         return render_to_response('contact.html',
                                   {'form': form, 'u': u,},
                                   context_instance=RequestContext(request))
       else:
         form=ContactForm()
         return render_to_response('contact.html',
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
        return render_to_response('entreprise.html', 
                                  {'form': form},
                                  context_instance=RequestContext(request))
     else:
       form=ContactForm()
       return render_to_response('entreprise.html',
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
