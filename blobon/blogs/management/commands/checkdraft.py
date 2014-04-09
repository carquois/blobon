from datetime import datetime
from accounts.models import UserProfile
from blogs.models import Post, Blog
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

import urllib2
from urlparse import urlparse

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

from django.conf import settings


class Command(NoArgsCommand):
  help = 'Check if draft is empty'

  def handle(self, **options):
       blogs = Blog.objects.filter(draft_notice=True)
       for blog in blogs:
         posts = Post.objects.filter(blog=blog).filter(is_ready=True).filter(status="D").filter(is_discarded=False).order_by('-pub_date')
         if not posts:
           blog_title = blog.title
           slug = blog.slug
           if blog.moderator_email:
             mailto = blog.moderator_email
           else:
             mailto = blog.creator.email
           from django.core.mail import EmailMultiAlternatives
           from django.template.loader import get_template
           from django.template import Context
           plaintext = get_template('blogs/email_empty_draft.txt')
           htmly     = get_template('blogs/email_empty_draft.html')

           d = Context({ 'blog_title': blog_title, 'slug': slug , })  

           subject = 'Your draft is empty'
           from_email = 'info@blobon.com'
           to = mailto
           text_content = plaintext.render(d)
           html_content = htmly.render(d)
           msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
           msg.attach_alternative(html_content, "text/html")
           msg.send()

