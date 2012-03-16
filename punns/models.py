from django.db import models


class Punn(models.Model):
    title = models.CharField(max_length=120)
    karma = models.IntegerField()
    source = models.CharField(max_length=300)
    created = models.DateTimeField()
    def __unicode__(self):
        return self.titre
