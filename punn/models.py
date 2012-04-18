from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #TODO https://github.com/simplegeo/python-oauth2
    oauth_token = models.CharField(max_length=200, blank=True)
    oauth_secret = models.CharField(max_length=200, blank=True)
    #Basic infos
    description = models.CharField(max_length=160, blank=True)
    avatar = models.URLField(max_length=300, blank=True)
    domain = models.URLField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    sites = models.ForeignKey(Site, blank=True, null=True)
    #Custom user design
    background_color = models.CharField(max_length=6, blank=True)
    well_color = models.CharField(max_length=6, blank=True)
    font_color = models.CharField(max_length=6, blank=True)
    link_color = models.CharField(max_length=6, blank=True)
    #Social infos
    facebook_profile = models.URLField(max_length=300, blank=True)
    twitter_oauth_token = models.CharField(max_length=120, blank=True)
    twitter_oauth_token_secret = models.CharField(max_length=120, blank=True)
    def __unicode__(self):
        return self.description

class App(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=140)
    website = models.URLField(max_length=300)
    author = models.ForeignKey(User)
    consumer_key = models.CharField(max_length=120)
    consumer_secret = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Punn(models.Model):
    #Basic infos
    title = models.CharField(max_length=140)
    base64id = models.CharField(max_length=140, blank=True)
    karma = models.IntegerField()
    source = models.URLField(max_length=300, blank=True)
    author = models.ForeignKey(User)
    original_punn = models.ForeignKey('self',  null=True, blank=True)
    app = models.ForeignKey(App)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    created = models.DateTimeField()
    pub_date = models.DateTimeField('date published',  null=True, blank=True)
    #Media infos
    thumbnail = models.URLField(max_length=300, blank=True)
    image = models.URLField(max_length=300, blank=True)
    content = models.CharField(max_length=10000, blank=True)
    youtube_id = models.CharField(max_length=30, blank=True)
    vimeo_id = models.CharField(max_length=30, blank=True)
    #Social infos
    facebook_publication_link = models.URLField(max_length=300, blank=True)
    tweet_link = models.URLField(max_length=300, blank=True)
    reddit_link = models.URLField(max_length=300, blank=True)
    #Adsense && Analytics
    analytics_id = models.CharField(max_length=30, blank=True)
    adsense_id = models.CharField(max_length=30, blank=True)
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


