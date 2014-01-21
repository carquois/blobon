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
        publish_draft(psot)
        publish_facebook_link(post)
        publish_twitter_link(post)
        if post.translated_title and up.fr_user:
          post.is_top = False
          post.save()
          new_post = Post(title=post.translated_title, author= up.fr_user, original_post = post, pic=post.pic, source=post.source, is_top=True, youtube_id=post.youtube_id)
          publish_draft(new_post)
          publish_facebook_link(new_post)
          publish_twitter_link(new_post)


def publish_draft(post):
        post.status = "P"
        post.pub_date = datetime.now()
        post.save()

def publish_twitter_link(post):
      up = UserProfile.objects.get(user=post.author)
      if up.twitter_oauth_token:
        twitter = Twython(APP_KEY, APP_SECRET,
                  up.twitter_oauth_token, up.twitter_oauth_token_secret)
        twitter.update_status(status="%s\n\nhttp://%s%s" % (post.title.encode('utf-8') , settings.MAIN_SITE_DOMAIN, post.get_absolute_url() ))

def publish_facebook_link(post):
      up = UserProfile.objects.get(user=post.author)
      graph = facebook.GraphAPI(up.fan_page_access_token)
      profile = graph.get_object("me")
      graph.put_object("me", "feed", link="http://%s%s" % (settings.MAIN_SITE_DOMAIN, post.get_absolute_url() ))
