from django.db import models

class User(models.Model):
    #Basic infos
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    avatar = models.URLField(max_length=300)
    created = models.DateTimeField()
    email = models.CharField(max_length=256)
    #Custom user design
    background_color = models.CharField(max_length=6)
    outside_color = models.CharField(max_length=6)
    inside_color = models.CharField(max_length=6)
    font_color = models.CharField(max_length=6)
    link_color = models.CharField(max_length=6)
    #Social infos
    facebook_profile = models.URLField(max_length=300, blank=True)
    twitter_oauth_token = models.CharField(max_length=120, blank=True)
    twitter_oauth_token_secret = models.CharField(max_length=120, blank=True)
    def __unicode__(self):
        return self.username

class Punn(models.Model):
    #Basic infos
    title = models.CharField(max_length=140)
    karma = models.IntegerField()
    views = models.IntegerField()
    source = models.URLField(max_length=300, blank=True)
    author = models.ForeignKey(User)
    original_author = models.ForeignKey(User, blank=True)
    original_punn = models.ForeignKey(Punn, blank=True)
    app = models.ForeignKey(App)
    created = models.DateTimeField()
    pub_date = models.DateTimeField('date published', blank=True)
    #Media infos
    thumbnail = models.URLField(max_length=300, blank=True)
    image = models.URLField(max_length=300, blank=True)
    youtube_id = models.CharField(max_length=30)
    vimeo_id = models.CharField(max_length=30)
    #Social infos
    facebook_publication_link = models.URLField(max_length=300, blank=True)
    tweet_link = models.URLField(max_length=300, blank=True)
    reddit_link = models.URLField(max_length=300, blank=True)
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


class App(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=140)
    website = models.URLField(max_length=300)
    consumer_key = models.CharField(max_length=120)
    consumer_secret = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name



