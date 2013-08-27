from datetime import datetime
import random

from accounts.models import UserProfile
from punns.models import Punn

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

def publish(frequency):
  for u in UserProfile.objects.all().distinct():
    if u.publication_frequency == frequency:
      p = Punn.objects.filter(author = u.user).filter(status='D')
      if p.count() > 0:

class Command(BaseCommand):
  args = '<frequency frequency ...>'
  help = 'Publish an article'

  def handle(self, *args, **options):
    for frequency in args:
      if frequency == '15m':
        publish('15m')
      if frequency == '30m':
        publish('30m')

