from datetime import datetime
from accounts.models import UserProfile
from blogs.models import Post

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
  args = '<username username ...>'
  help = 'Publish a fan page'

  def handle(self, *args, **options):
    for username in args:
      u = User.objects.get(username=username)
      up = UserProfile.objects.get(user=u)
      p = Post.objects.filter(author=u).filter(status="D").order_by('-pub_date')[:1]
      if p.count() >= 1:
        post = p[0]
        publish_draft(post)
        if post.translated_title and up.fr_user: 
          post.is_top = False
          post.save()
          new_post = Post(title=post.translated_title, author= up.fr_user, blog=post.blog, pic=post.pic, source=post.source, is_top=False)
          publish_draft(new_post)


def publish_draft(post):
        post.status = "P"
        post.pub_date = datetime.now()
        post.save()
