from django.db import models
from django.utils.translation import ugettext as _

class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField(max_length=10000, blank=True)
    #Datetime infos
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    #Media
    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
        return ('news.views.news', [str(self.id)])
