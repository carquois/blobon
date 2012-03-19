from django.db import models


class Punn(models.Model):
    title = models.CharField(max_length=140)
    karma = models.IntegerField()
    source = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title
