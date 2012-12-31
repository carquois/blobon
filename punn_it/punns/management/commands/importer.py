from httplib2 import Http
from urllib import urlencode
import string, os, sys, getopt
from xml.dom import minidom
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from punns.models import Punn
import datetime
from accounts.models import UserProfile

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
      filters='ga:pagePath==/p/%s/' % path,
      max_results='1')

def countviews(number_to_count):
    service = sample_utils.initialize_service()
    user = UserProfile.objects.get(pk=3)
    for p in Punn.objects.filter(author=user).filter(status='P').order_by('-pub_date')[:number_to_count]:
      try:
        print "Id : %s" % p.id
        results = get_api_query(service, p.base62id).execute()
        for row in results.get('rows'):
          p.views = row[0]
          print "Views : %s" % p.views
          p.save()
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
      print node.getElementsByTagName('title')[0].firstChild.data
      for meta in node.getElementsByTagName('wp:postmeta'):
        if meta.getElementsByTagName('wp:meta_key')[0].firstChild.data == "via":
          try: 
            print meta.getElementsByTagName('wp:meta_value')[0].firstChild.data
          except AttributeError:
            print "Pas de source, pas grave"
        if meta.getElementsByTagName('wp:meta_key')[0].firstChild.data == "image":
          try: 
            print meta.getElementsByTagName('wp:meta_value')[0].firstChild.data
          except AttributeError:
            print "Pas d'image, on laisse faire"
        #img_temp = NamedTemporaryFile(delete=True)
        #img_temp.write(urllib2.urlopen(meta.getElementsByTagName('wp:meta_value')[0].firstChild.data).read())
        #img_temp.flush()
        #filename = urlparse(meta.getElementsByTagName('wp:meta_value')[0].firstChild.data).path.split('/')[-1]
        #ext = filename.split('.')[-1]
        #prefix = new_punn.base62id
        #filename = "%s.%s" % (prefix, ext)
        #new_punn.pic.save(filename, File(img_temp))

