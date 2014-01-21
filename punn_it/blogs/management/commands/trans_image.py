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
      os.chdir(settings.MEDIA_ROOT)
      if p.count() >= 1:
        post = p[0]
        ext = post.pic.name.split('.')[-1]
        if ext != "gif":
          publish_draft(post)
          publish_facebook_image(post)
          if post.translated_title and up.fr_user:
            post.is_top = False
            post.save()
            new_post = Post(title=post.translated_title, author= up.fr_user, original_post = post, pic=post.pic, source=post.source, is_top=True)
            publish_draft(new_post)
            publish_twitter_image(new_post)
            publish_facebook_image(new_post)
          publish_twitter_image(post)
        elif ext == "gif":
            publish_draft(post)
            if post.translated_title and up.fr_user:
              post.is_top = False
              post.save()
              new_post = Post(title=post.translated_title, author= up.fr_user, original_post = post, pic=post.pic, source=post.source, is_top=True)
              publish_draft(new_post)

def publish_draft(post):
        post.status = "P"
        post.pub_date = datetime.now()
        post.save()

def publish_twitter_image(post):
      up = UserProfile.objects.get(user=post.author)
      if up.twitter_oauth_token:
        twitter = Twython(APP_KEY, APP_SECRET,
                  up.twitter_oauth_token, up.twitter_oauth_token_secret)
        photo = open(str(post.pic.name), 'rb')
        twitter.update_status_with_media(status=post.title.encode('utf-8'), media=photo)

def publish_facebook_image(post):
      up = UserProfile.objects.get(user=post.author)
      graph = facebook.GraphAPI(up.fan_page_access_token)
      profile = graph.get_object("me")
      response = graph.put_photo(open(str(post.pic.name)), '%s\n\nhttp://%s%s' % (post.title.encode('utf-8') , settings.MAIN_SITE_DOMAIN, post.get_absolute_url() ))
