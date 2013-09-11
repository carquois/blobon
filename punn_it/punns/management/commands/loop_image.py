from datetime import datetime
from accounts.models import UserProfile
from punns.models import Punn

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
      p = Punn.objects.filter(author=u).filter(status="P").order_by('?')[:1]
      os.chdir(settings.MEDIA_ROOT)
      if p.count() >= 1:
        punn = p[0]
        publish_facebook_image(punn)
        publish_twitter_image(punn)

def publish_twitter_image(punn):
      up = UserProfile.objects.get(user=punn.author)
      if up.twitter_oauth_token:
        twitter = Twython(APP_KEY, APP_SECRET,
                  up.twitter_oauth_token, up.twitter_oauth_token_secret)
        photo = open(str(punn.pic.name), 'rb')
        twitter.update_status_with_media(status=punn.title.encode('utf-8'), media=photo)

def publish_facebook_image(punn):
      up = UserProfile.objects.get(user=punn.author)
      graph = facebook.GraphAPI(up.fan_page_access_token)
      profile = graph.get_object("me")
      response = graph.put_photo(open(str(punn.pic.name)), '%s\n\nhttp://%s%s' % (punn.title.encode('utf-8') , settings.MAIN_SITE_DOMAIN, punn.get_absolute_url() ))
