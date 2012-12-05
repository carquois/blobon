from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from punns.models import Punn

class Command(BaseCommand):
  args = '<frequency frequency ...>'
  help = 'Publish an article'

  def handle(self, *args, **options):
    for frequency in args: 
      if frequency == '15m':
        self.stdout.write('15m')
      if frequency == '30m':
        self.stdout.write('30m')
      if frequency == '1h':
        self.stdout.write('1h')
      if frequency == '3h':
        self.stdout.write('3h')


    #for u in User.objects.all().distinct():
    #  print(u.username)
    #  p = Punn.objects.filter(author = u).filter(status='D')
    #  print(p)
    #  if p.count() > 0:
    #    e = Punn.objects.get(id=p[0].pk)
    #    e.status = 'P'
    #    e.save()
    #self.stdout.write('Success')
