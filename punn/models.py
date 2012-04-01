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
    thumbnail = models.URLField(max_length=300)
    CONTENT_TYPES = (
        ('I', 'Image'),
        ('V', 'Video'),
        ('L', 'Link'),
        ('A', 'Article'),
        ('S', 'Status'),
    )
    content_type = models.CharField(max_length=1, choices=CONTENT_TYPES)
    karma = models.IntegerField()
    source = models.URLField(max_length=300)
    created = models.DateTimeField()
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(User)
    punn = models.ForeignKey(Punn)
    karma = models.IntegerField()
    source = models.URLField(max_length=300)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.content









