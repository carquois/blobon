from accounts.models import UserProfile
from punns.models import Punn

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

import random


def publish(frequency):
  for u in UserProfile.objects.all().distinct():
    if u.publication_frequency == frequency:
      p = Punn.objects.filter(author = u.user).filter(status='D')
      if p.count() > 0:
        e = Punn.objects.get(id=p[random.randrange(0,p.count())].pk)
        e.status = 'P'
        e.save()

class Command(BaseCommand):
  args = '<frequency frequency ...>'
  help = 'Publish an article'

  def handle(self, *args, **options):
    for frequency in args:
      if frequency == '15m':
        publish('15m')
      if frequency == '30m':
        publish('30m')
      if frequency == '1h':
        publish('1h')
      if frequency == '3h':
        publish('3h')

