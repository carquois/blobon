from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from punns.models import Punn
from accounts.models import UserProfile

class Command(BaseCommand):
  args = '<frequency frequency ...>'
  help = 'Publish an article'

  def handle(self, *args, **options):
    for frequency in args:
      if frequency == '15m':
        for u in UserProfile.objects.all().distinct():
          if u.publication_frequency == '15m':
            p = Punn.objects.filter(author = u.user).filter(status='D')
            if p.count() > 0:
              e = Punn.objects.get(id=p[0].pk)
              e.status = 'P'
              e.save()
      if frequency == '30m':
        for u in UserProfile.objects.all().distinct():
          if u.publication_frequency == '30m':
            p = Punn.objects.filter(author = u.user).filter(status='D')
            if p.count() > 0:
              e = Punn.objects.get(id=p[0].pk)
              e.status = 'P'
              e.save()

