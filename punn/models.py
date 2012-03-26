from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    avatar = models.URLField(max_length=300)
    created = models.DateTimeField()
    email = models.CharField(max_length=256)
    def __unicode__(self):
        return self.username

class Punn(models.Model):
    title = models.CharField(max_length=140)
    image = models.URLField(max_length=300)
    karma = models.IntegerField()
    source = models.URLField(max_length=300)
    created = models.DateTimeField()
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title





