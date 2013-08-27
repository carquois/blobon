from datetime import datetime
import random

from accounts.models import UserProfile
from punns.models import Punn
from earnings.models import Earning

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
  args = '<amout amount ...>'
  help = 'Give an amount to everybody'

  def handle(self, *args, **options):
    for amount in args:
      for u in User.objects.all().distinct():
        e = Earning(user=u, amount=amount, date=datetime.now())
        e.save()
