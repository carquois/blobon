from datetime import datetime
from accounts.models import UserProfile
from blogs.models import Post, Rss
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

import urllib2
from urlparse import urlparse

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

from django.conf import settings


class Command(NoArgsCommand):
  help = 'Rss auto post'

  def handle(self, **options):
       rsss = Rss.objects.all()
       for rss in rsss:
         blog = rss.blog
         url = rss.feed_url
         import feedparser
         from BeautifulSoup import BeautifulSoup
         feed = feedparser.parse(url)
         parsed_feed = []
         for entry in feed.entries:
           response = urllib2.urlopen(entry.link)
           soup = BeautifulSoup(response.read())
           entry.img = []
           for image in soup.findAll("img"):
             entry.img.append(image['src'])
           post, created = Post.objects.get_or_create(author=blog.creator, blog=blog, source=entry.link)
           post.status = "D"
           if len(entry.title) > 140:
             post.title = "Title to long"
           else:
             post.title = entry.title
           post.is_ready = False
           post.save()
           img_url = "%s%s" % ('http:', entry.img[0])
           img_temp = NamedTemporaryFile(delete=True)
           img_temp.write(urllib2.urlopen(img_url).read())
           img_temp.flush()
           filename = urlparse(entry.img[0]).path.split('/')[-1]
           ext = filename.split('.')[-1]
           prefix = post.base62id
           filename = "%s.%s" % (prefix, ext)
           post.pic.save(filename, File(img_temp))
