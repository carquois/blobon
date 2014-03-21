from datetime import datetime
from accounts.models import UserProfile
from blogs.models import Post, Blog, Subscription, Info_email

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
  args = '<info_email_id info_email_id ...>'
  help = 'Auto send daily info-letter'

  def handle(self, *args, **options):
    for info_email_id in args:
      info_email = Info_email.objects.get(id=info_email_id)
      blog = info_email.blog
      subject = info_email.subject
      text_content = info_email.message
      from_email = 'vincegothier@gmail.com'
      recipient_list = [] 
      if info_email.subscribers == 'A':
        for subscription in Subscription.objects.filter(blog=blog):
          recipient_list.append(subscription.email)
        from django.core.mail import EmailMultiAlternatives
        msg = EmailMultiAlternatives(subject, text_content, from_email, bcc=recipient_list)
        msg.send()
      else:
        for subscription in Subscription.objects.filter(blog=blog).filter(is_new=True):
          recipient_list.append(subscription.email)
          subscription.is_new = False
          subscription.save()
        from django.core.mail import EmailMultiAlternatives
        msg = EmailMultiAlternatives(subject, text_content, from_email, bcc=recipient_list)
        msg.send()


