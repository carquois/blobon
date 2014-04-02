from datetime import datetime
from accounts.models import UserProfile
from blogs.models import Post, Blog

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from social_auth.models import UserSocialAuth
import os
from twython import Twython

from django.conf import settings


class Command(BaseCommand):
  args = '<rssblog rssblog ...>'
  help = 'Delete feed posts'

  def handle(self, *args, **options):
    for rssblog in args:
#      u = User.objects.get(username=username)
#      up = UserProfile.objects.get(user=u)
      b = Blog.objects.get(slug=rssblog)
      ps = Post.objects.filter(blog=b).filter(status="P").order_by('-pub_date')
      if ps.count() >= 1:
        for post in ps:
          post.delete()


