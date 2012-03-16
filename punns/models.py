from django.db import models
from django.contrib.sites.models import Site

class User(models.Model):
    name = models.CharField(max_length=20)
    avatar = models.CharField(max_length=300)
    created = models.DateTimeField()
    email = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class Punn(models.Model):
    author = models.ForeignKey(User)
    titre = models.CharField(max_length=120)
    sites = models.ManyToManyField(Site)
    karma = models.IntegerField()
    source = models.CharField(max_length=300)
    created = models.DateTimeField()
    def __unicode__(self):
        return self.titre

class ContentType(models.Model):
    CONTENT_TYPES = (
        ('P', 'Punn'),
        ('C', 'Comment'),
        ('U', 'User'),
        ('S', 'Sites'),
    )
    content_type = models.CharField(max_length=1, choices=CONTENT_TYPES)

class Comment(models.Model):
    author = models.ForeignKey(User)
    punn = models.ForeignKey(Punn)
    karma = models.IntegerField()
    content = models.CharField(max_length=120)
    created = models.DateTimeField()
    def __unicode__(self):
        return self.content

class Alert(models.Model):
    content = models.CharField(max_length=120)


class Vote(models.Model):
    voter = models.ForeignKey(User)
    VOTE_CHOICES = (
        ('U', 'Up'),
        ('D', 'Down'),
    )
    punn = models.ForeignKey(Punn)
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES)
    created = models.DateTimeField()
    content_type = models.ForeignKey(ContentType)

class Subscription(models.Model):
    suscriber = models.ForeignKey(User)
    SUBSCRIPTION_CHOICES = (
        ('S', 'Subscribe'),
        ('U', 'Unsubscribe'),
    )
    subscription_type = models.CharField(max_length=1, choices=SUBSCRIPTION_CHOICES)
    content_type = models.ForeignKey(ContentType)
    created = models.DateTimeField()
