
from accounts.models import UserProfile
from punns.models import Punn

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from social_auth.models import UserSocialAuth
import facebook
import os

from django.core.mail import send_mail

class Command(BaseCommand):
  args = '<username username ...>'
  help = 'Show fan pages an access token for user'

  def handle(self, *args, **options):
    for username in args:
      u = User.objects.get(username=username)
      instance = UserSocialAuth.objects.filter(provider='facebook').filter(user=u)
      graph = facebook.GraphAPI(instance[0].tokens['access_token'])
      pages = graph.get_connections("me", "accounts")
      for page in pages['data']:
        print page['name']
        print page['access_token']
      
