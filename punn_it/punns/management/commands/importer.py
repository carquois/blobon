from django.core.files import File
from urlparse import urlparse
import urllib2
from httplib2 import Http
from urllib import urlencode
import string, os, sys, getopt
from xml.dom import minidom
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from punns.models import Punn
import datetime
from accounts.models import UserProfile
from django.core.files.temp import NamedTemporaryFile

import sys
import sample_utils

from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError


TABLE_ID = 'ga:36957805'


def get_api_query(service, path):
  return service.data().ga().get(
      ids=TABLE_ID,
      start_date='2010-10-01',
      end_date=str(datetime.date.today()),
      metrics='ga:pageviews',
      filters='ga:pagePath==/%s' % path,
      max_results='1')

def countviews(path):
    service = sample_utils.initialize_service()
    try:
      results = get_api_query(service, path).execute()
      for row in results.get('rows'):
        print row[0]
      return row[0] 
    except TypeError, error:
      # Handle errors in constructing a query.
      print ('There was an error in constructing your query : %s' % error)
    except HttpError, error:
      # Handle API errors.
      print ('Arg, there was an API error : %s : %s' %
             (error.resp.status, error._get_reason()))
    except AccessTokenRefreshError:
      # Handle Auth errors.
      print ('The credentials have been revoked or expired, please re-run '
             'the application to re-authorize')

class Command(BaseCommand):
  help = 'Import the articles'

  def handle(self, *args, **options):
    dom = minidom.parse("gab.xml")
    for node in dom.getElementsByTagName('item'):
      print "Title : "
      print node.getElementsByTagName('title')[0].firstChild.data
      print "Wordpress id : " 
      print node.getElementsByTagName('wp:post_id')[0].firstChild.data
      print "Page views : " 
      countviews(node.getElementsByTagName('wp:post_id')[0].firstChild.data)
      print "Post date : " 
      print node.getElementsByTagName('wp:post_date')[0].firstChild.data
      for meta in node.getElementsByTagName('wp:postmeta'):
        if meta.getElementsByTagName('wp:meta_key')[0].firstChild.data == "image":
          try: 
            print meta.getElementsByTagName('wp:meta_value')[0].firstChild.data
            user = User.objects.get(pk=3)
            new_punn = Punn(author=user, title=node.getElementsByTagName('title')[0].firstChild.data)
            new_punn.save()
            print "New punn id"
            print new_punn.id
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(meta.getElementsByTagName('wp:meta_value')[0].firstChild.data).read())
            img_temp.flush()
            filename = urlparse(meta.getElementsByTagName('wp:meta_value')[0].firstChild.data).path.split('/')[-1]
            ext = filename.split('.')[-1]
            prefix = new_punn.base62id
            filename = "%s.%s" % (prefix, ext)
            new_punn.pic.save(filename, File(img_temp))
            try:
              new_punn.views = int(countviews(node.getElementsByTagName('wp:post_id')[0].firstChild.data))
              new_punn.save() 
            except TypeError:
              new_punn.views = 0
              print "TypeError, views = 0"
            for meta in node.getElementsByTagName('wp:postmeta'):
              if meta.getElementsByTagName('wp:meta_key')[0].firstChild.data == "via":
                new_punn.source = meta.getElementsByTagName('wp:meta_value')[0].firstChild.data
            new_punn.status = 'P'
            new_punn.save() 
          except AttributeError:
            print "Pas d'image, on laisse faire"
