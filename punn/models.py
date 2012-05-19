from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, CharField, PasswordInput
from punn.utils import BASE10, BASE62, baseconvert

class UserForm(ModelForm):
    username = CharField(help_text="Don't worry, you can change it later.")
    password = CharField(help_text="Be tricky.",widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #Basic infos
    description = models.CharField(max_length=160, blank=True)
    avatar = models.URLField(max_length=300, blank=True)
    domain = models.URLField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    sites = models.ForeignKey(Site, blank=True, null=True)
    LANGUAGES_CHOICES = (
        ('en', 'English'),
        ('fr', 'Français'),
        ('qc', 'Québécois'),
    )
    language = models.CharField(default="en", max_length=2, choices=LANGUAGES_CHOICES)
    #Custom user design
    background_color = models.CharField(max_length=6, blank=True)
    well_color = models.CharField(max_length=6, blank=True)
    font_color = models.CharField(max_length=6, blank=True)
    link_color = models.CharField(max_length=6, blank=True)
    #Social infos
    facebook_profile = models.URLField(max_length=300, blank=True)
    twitter_profile = models.URLField(max_length=300, blank=True)
    #Google Infos
    analytics_account = models.CharField(max_length=50, blank=True)
    def __unicode__(self):
        return self.description

class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

#TODO PUT THE DEFAULT THUMBNAILS
class Story(models.Model):
    thumbnail = models.ImageField(upload_to='pics', blank=True)
    content = models.TextField(max_length=10000, blank=True)

class Image(models.Model):
    thumbnail = models.ImageField(upload_to='pics', blank=True)
    image = models.ImageField(upload_to='pics', blank=True)

class Video(models.Model):
    thumbnail = models.ImageField(upload_to='pics', blank=True)
    youtube_id = models.CharField(max_length=30, blank=True)
    vimeo_id = models.CharField(max_length=30, blank=True)

class Audio(models.Model):
    thumbnail = models.ImageField(upload_to='pics', blank=True)
    audio = models.FileField(upload_to='audio', blank=True)

class Tweet(models.Model):
    thumbnail = models.ImageField(upload_to='pics', blank=True)

#The Shared Punn Model
class Punn(models.Model):
    #Basic infos
    title = models.CharField(max_length=140)
    base62id = models.CharField(max_length=140, blank=True)
    karma = models.IntegerField(default=0)
    source = models.URLField(max_length=300, blank=True)
    author = models.ForeignKey(User)
    original_punn = models.ForeignKey('self',  null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now = True,  null=True, blank=True)
    PUNN_TYPES = (
        ('i', 'Image'),
        ('v', 'Video'),
        ('a', 'Audio'),
        ('t', 'Tweet'),
        ('s', 'Story'),
    )
    punn_type = models.CharField(default="1", max_length=2, choices=PUNN_TYPES)
    image = models.ForeignKey(Image,  null=True, blank=True)
    video = models.ForeignKey(Video,  null=True, blank=True)
    audio = models.ForeignKey(Audio,  null=True, blank=True)
    tweet = models.ForeignKey(Tweet,  null=True, blank=True)
    story = models.ForeignKey(Story,  null=True, blank=True)
    #Media infos
    #Social infos
    facebook_publication_link = models.URLField(max_length=300, blank=True)
    tweet_link = models.URLField(max_length=300, blank=True)
    reddit_link = models.URLField(max_length=300, blank=True)
    def __unicode__(self):
        return self.title
    def save(self):
        super(Punn, self).save()
        if not self.base62id:
            self.base62id = baseconvert(str(self.id),BASE10,BASE62)
            self.save()
    @models.permalink
    def get_absolute_url(self):
        return ('punn.views.single', [str(self.base62id)])


class Comment(models.Model):
    content = models.TextField(max_length=10000)
    base62id = models.CharField(max_length=140, blank=True)
    author = models.ForeignKey(User)
    punn = models.ForeignKey(Punn)
    karma = models.IntegerField(default=0)
    parent = models.ForeignKey('self',  null=True, blank=True)
    source = models.URLField(max_length=300, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now = True,  null=True, blank=True)
    def __unicode__(self):
        return self.content
    def save(self):
        super(Comment, self).save()
        if not self.base62id:
            self.base62id = baseconvert(str(self.id),BASE10,BASE62)
            self.save()
    @models.permalink
    def get_absolute_url(self):
        return ('punn.views.comment', [str(self.base62id)])

