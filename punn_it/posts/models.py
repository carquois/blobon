#!/usr/bin/env python
# -*- coding: utf-8 -*-

###IMPORTS###
#Django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from sorl.thumbnail import ImageField

from blogs.models import Blog

STATUS = (
    ('P', 'Publish'),
    ('D', 'Draft'),
)

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    filename = "%s.%s" % (prefix, ext)
    return os.path.join('', filename)

class Post(models.Model):
    author = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    
class BlogPost(Post):
    blog = models.ForeignKey(Blog, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
    content = models.TextField(verbose_name=_("Content"),max_length=10000, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS, default="P")
    def __unicode__(self):
        return self.title

class Image(Post):
    status = models.CharField(max_length=2, choices=STATUS, null=True, blank=True)
    title = models.CharField(verbose_name=_("Titre"), max_length=140, blank=True)
    translated_title = models.CharField(verbose_name=_("Titre traduit"), max_length=140, blank=True)
    base62id = models.CharField(max_length=140, blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    karma = models.IntegerField(default=0)
    views = models.IntegerField(default=0, blank=True)
    source = models.URLField(verbose_name=_("Source"), max_length=300, blank=True)
    original_punn = models.ForeignKey('self',  null=True, blank=True)
    content = models.TextField(verbose_name=_("Contenu"),max_length=10000, blank=True)
    is_video = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)
    publish_on_facebook = models.BooleanField(default=False)
    youtube_id = models.CharField(max_length=50, null=True, blank=True)
    pic = ImageField(verbose_name=_("Image"), upload_to=get_file_path, null=True, blank=True)
    def __unicode__(self):
        return self.title




