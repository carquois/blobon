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
#      u = User.objects.get(username=username)
#      up = UserProfile.objects.get(user=u)
      b = Blog.objects.get(slug=bl)
      tb = b.translation
      p = Post.objects.filter(blog=b).filter(is_discarded=False).filter(status="D").filter(is_ready=True).order_by('-pub_date')[:1]
      if p.count() >= 1:
        post = p[0]
        publish_draft(post)
        publish_twitter_link(post)
        if post.translated_title and post.blog.translation and post.translated_content and post.youtube_id: 
          post.save()
          new_post = Post(title=post.translated_title, content=post.translated_content, youtube_id=post.youtube_id, author=tb.creator, blog=post.blog.translation, pic=post.pic, source=post.source, is_top=True)
          publish_draft(new_post)
          publish_twitter_link(new_post)
        elif post.translated_title and post.blog.translation and post.youtube_id:
          post.save()
          new_post = Post(title=post.translated_title, youtube_id=post.youtube_id, author=tb.creator, blog=post.blog.translation, pic=post.pic, source=post.source, is_top=True)
          publish_draft(new_post)
          publish_twitter_link(new_post)

        elif post.translated_title and post.blog.translation and post.translated_content:
          post.save()
          new_post = Post(title=post.translated_title, content=post.translated_content, author=tb.creator, blog=post.blog.translation, pic=post.pic, source=post.source, is_top=True)
          publish_draft(new_post)
          publish_twitter_link(new_post)
        elif post.translated_title and post.blog.translation:
          post.save()
          new_post = Post(title=post.translated_title, author=tb.creator, blog=post.blog.translation, pic=post.pic, source=post.source, is_top=True)
          publish_draft(new_post)
          publish_twitter_link(new_post)

def publish_draft(post):
        post.status = "P"
        post.is_top = True 
        post.pub_date = datetime.now()
        post.save()

def publish_twitter_link(post):
      if post.blog.twitter_oauth_token:
        twitter = Twython(APP_KEY, APP_SECRET,
                  post.blog.twitter_oauth_token, post.blog.twitter_oauth_token_secret)
        twitter.update_status(status="%s\n\nhttp://%s%s" % (post.title.encode('utf-8') , settings.MAIN_SITE_DOMAIN, post.get_absolute_url() ))

def publish_facebook_link(post):
      up = UserProfile.objects.get(user=post.author)
      graph = facebook.GraphAPI(up.fan_page_access_token)
      profile = graph.get_object("me")
      graph.put_object("me", "feed", link="http://%s%s" % (settings.MAIN_SITE_DOMAIN, post.get_absolute_url() ))


