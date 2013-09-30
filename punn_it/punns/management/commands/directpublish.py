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
      p = Punn.objects.filter(author=u).filter(status="D").order_by('-pub_date')[:1]
      if p.count() >= 1:
        punn = p[0]
        publish_draft(punn)
        if punn.translated_title and up.fr_user: 
          punn.is_top = False
          punn.save()
          new_punn = Punn(title=punn.translated_title, author= up.fr_user, original_punn = punn, pic=punn.pic, source=punn.source, is_top=True)
          publish_draft(new_punn)


def publish_draft(punn):
        punn.status = "P"
        punn.pub_date = datetime.now()
        punn.save()
