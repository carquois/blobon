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
      start_date='2012-10-01',
      end_date=str(datetime.date.today()),
      metrics='ga:pageviews',
      filters='ga:pagePath==/p/%s/' % path,
      max_results='1')


class Command(BaseCommand):
  help = 'Count the views'

  def handle(self, *args, **options):
    service = sample_utils.initialize_service()
    user = UserProfile.objects.get(pk=3)
    for p in Punn.objects.filter(author=user).filter(status='P').order_by('-pub_date')[:100]:
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
#    SOURCE_APP_NAME = 'Blobon view counter'
#    my_client = gdata.analytics.client.AnalyticsClient(source=SOURCE_APP_NAME)
#    my_client.client_login(
#        'gabrieldancause@gmail.com',
#        'a74108520S',
#        source=SOURCE_APP_NAME,
#        service=my_client.auth_service,
#        account_type = 'GOOGLE',
#    )
#    token = my_client.auth_token
#    account_query = gdata.analytics.client.AccountFeedQuery()
#    for p in Punn.objects.filter(status='P').order_by('-pub_date')[:1500]:
#      data_query = gdata.analytics.client.DataFeedQuery({
#        'ids': 'ga:64078171',
#        'metrics': 'ga:pageviews',
#        'filters': 'ga:pagePath==/p/%s/' % p.base62id,
#        'start-date': '2012-10-01',
#        'end-date': '%s' % time.strftime("%Y-%m-%d"),
#      }) 
#      feed = my_client.GetDataFeed(data_query)
#      result = [(x.name, x.value) for x in feed.entry[0].metric]
#      p.views = x.value
#      p.save()
    self.stdout.write('Success')
