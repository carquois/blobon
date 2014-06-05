from datetime import datetime, timedelta
from accounts.models import UserProfile
from blogs.models import Post, Blog

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

from social_auth.models import UserSocialAuth
import facebook
import os
from twython import Twython

from django.core.mail import send_mail
from django.conf import settings

from accounts.views import APP_KEY, APP_SECRET

class Command(NoArgsCommand):
  help = 'Auto-publish post depending on frequency and exclusion time'

  def handle(self, **options):
       blogs = Blog.objects.filter(is_online=True).exclude(frequency__isnull=True).exclude(frequency__exact='')
       for blog in blogs:
         last_draft = Post.objects.filter(blog=blog).filter(is_discarded=False).filter(status="D").filter(is_ready=True).order_by('pub_date')[:1]
         last_publish = Post.objects.filter(blog=blog).filter(is_discarded=False).filter(status="P").filter(is_ready=True).order_by('-pub_date')[:1]
         if last_draft.count() >=1:
           now = datetime.now()
           last_publish_datetime = last_publish[0].pub_date
           tdelta = now - last_publish_datetime
           minutes_diff = tdelta.seconds/60           
           if blog.frequency == "15m" or blog.frequency == "30m":
             freq = blog.frequency.replace('m', '')
           else:
             a = blog.frequency.replace('h', '')   
             freq = int(a) * 60
           if blog.exclusion_start and blog.exclusion_end:
             s = blog.exclusion_start.replace(':','') 
             e = blog.exclusion_end.replace(':','')
             start = int(s)/100 
             end = int(e)/100
             y = now.year
             m = now.month
             h = now.hour
             d = now.day
             if int(start) == int(end):
               if int(minutes_diff) >= int(freq):
                 post = last_draft[0]
                 post.status = "P"
                 post.pub_date = datetime.now()
                 post.save()
               else:
                 print "exclu1"
             elif int(start) == now.hour or int(end) == now.hour + 1:
               print "exclu2"  
             elif int(start) < int(end): 
               exc_begin = datetime(y,m,d,start)
               exc_end = datetime(y,m,d,end)
               if exc_begin < now < exc_end:
                 print "exclu3"
               else:
                 if int(minutes_diff) >= int(freq):
                   post = last_draft[0]
                   post.status = "P"
                   post.pub_date = datetime.now()
                   post.save()
                 else:
                   print "exclu4"
             elif int(start) > int(end) and now.hour <= int(start):
               d2 = now.day-1
               exc_begin = datetime(y,m,d2,start)
               exc_end = datetime(y,m,d,end)   
               if exc_begin < now < exc_end:
                 print "exclu5"
               else:
                 if int(minutes_diff) >= int(freq):
                   post = last_draft[0]
                   post.status = "P"
                   post.pub_date = datetime.now()
                   post.save()
                 else:
                   print blog
                   print freq
                   print minutes_diff
                   print "exclu6"
                   print exc_begin
                   print exc_end
                   print now
             elif int(start) > int(end) and now.hour > int(start):
               d3 = now.day+1
               exc_begin = datetime(y,m,d,start)
               exc_end = datetime(y,m,d3,end)
               if exc_begin < now < exc_end:
                 print "exclu7"
               else:
                 if int(minutes_diff) >= int(freq):
                   post = last_draft[0]
                   post.status = "P"
                   post.pub_date = datetime.now()
                   post.save()
                 else:
                   print "exclu8"
           else:
             if int(minutes_diff) >= int(freq):
               post = last_draft[0]
               post.status = "P"
               post.pub_date = datetime.now()
               post.save()
             else:
               print "exclu9"
