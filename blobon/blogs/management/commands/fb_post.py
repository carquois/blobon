from datetime import datetime
from accounts.models import UserProfile
from blogs.models import Post, Blog

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from social_auth.models import UserSocialAuth
import facebook
import os
from twython import Twython

from django.core.mail import send_mail
from django.conf import settings

from accounts.views import APP_KEY, APP_SECRET

class Command(BaseCommand):
  args = '<bl bl ...>'
  help = 'Publish a fan page'

  def handle(self, *args, **options):
    for bl in args:
      b = Blog.objects.get(slug=bl)
      p = Post.objects.filter(blog=b).filter(is_discarded=False).filter(status="P").filter(is_ready=True).order_by('-pub_date')[:1]
      if p.count() >= 1:
        post = p[0]
      if b.fb_page_access_token:
        publish_facebook_link(post)

def publish_facebook_link(post):
      if post.blog.fb_page_access_token: 
        bl = post.blog 
        graph = facebook.GraphAPI(bl.fb_page_access_token)
        profile = graph.get_object("me")
        if bl.custom_domain:
          domain = bl.custom_domain
        else:
          main = "blobon.com"
          domain = "%s.%s" % (bl.slug,main)
        graph.put_object("me", "feed", link="http://%s%s" % (domain, post.get_absolute_url() ))


