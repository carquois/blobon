from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from punns.models import Punn
import gdata.analytics.client  

class Command(BaseCommand):
  help = 'Count the views'

  def handle(self, *args, **options):
    SOURCE_APP_NAME = 'Blobon view counter'
    my_client = gdata.analytics.client.AnalyticsClient(source=SOURCE_APP_NAME)
    my_client.client_login(
        'gabrieldancause@gmail.com',
        'a74108520S',
        source=SOURCE_APP_NAME,
        service=my_client.auth_service,
        account_type = 'GOOGLE',
    )
    token = my_client.auth_token
    account_query = gdata.analytics.client.AccountFeedQuery()
    for p in Punn.objects.filter(status='P').order_by('-pub_date')[:5]:
      data_query = gdata.analytics.client.DataFeedQuery({
        'ids': 'ga:64078171',
        'metrics': 'ga:pageviews',
        'filters': 'ga:pagePath==/p/%s/' % p.base62id,
        'start-date': '2012-10-01',
        'end-date': '2012-10-15',
      }) 
      feed = my_client.GetDataFeed(data_query)
      result = [(x.name, x.value) for x in feed.entry[0].metric]
      self.stdout.write(str(result))
    self.stdout.write('Success')
