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
      graph = facebook.GraphAPI(up.fan_page_access_token)
      profile = graph.get_object("me")
      p = Punn.objects.filter(author=u).filter(status="D")[:1]
      if p.count() >= 1:
        punn = p[0]
        punn.status = "P"
        punn.pub_date = datetime.now()
        punn.save()
        graph.put_object("me", "feed", link="http://%s%s" % (settings.MAIN_SITE_DOMAIN, punn.get_absolute_url() ))
        if up.twitter_oauth_token:
          twitter = Twython(APP_KEY, APP_SECRET,
                    up.twitter_oauth_token, up.twitter_oauth_token_secret)
          twitter.update_status(status="%s\n\nhttp://%s%s" % (punn.title.encode('utf-8') , settings.MAIN_SITE_DOMAIN, punn.get_absolute_url() ))
