#!/usr/bin/env python
# -*- coding: utf-8 -*-

###IMPORTS###
#Django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from punns.utils import BASE10, BASE62, baseconvert

import uuid
import os
from random import choice
from sorl.thumbnail import ImageField

PRIVACY = (
    ('Pu', 'Public'),
    ('Pr', 'Private'),
)

STATUS = (
    ('P', 'Publish'),
    ('D', 'Draft'),
)

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    filename = "%s.%s" % (prefix, ext)
    return os.path.join('', filename)

def get_file_path_0(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('0')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_1(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('1')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_2(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('2')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_3(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('3')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_4(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('4')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_5(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('5')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_6(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('6')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_7(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('7')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

class Blog(models.Model):
    creator = models.ForeignKey(User, null=True)
    is_open = models.BooleanField(default=False)
    slug = models.SlugField(verbose_name=_("URL"), max_length=30, unique=True)
    title = models.CharField(verbose_name=_("Title"), max_length=140)
    password = models.CharField(verbose_name=_("Password"), max_length=140, blank=True)
    custom_domain = models.CharField(verbose_name=_("Custom domain"), max_length=300, blank=True)
    description = models.CharField(verbose_name=_("Description"), max_length=500, blank=True)
    translation = models.ForeignKey('self',  null=True, blank=True)
    def __unicode__(self):
        return self.title

class Page(models.Model):
    blog = models.ForeignKey(Blog, null=True)
    author = models.ForeignKey(User, null=True)
    status = models.CharField(max_length=2, choices=STATUS)
    title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
    content = models.TextField(verbose_name=_("Content"),max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    def __unicode__(self):
        return self.title

class Category(models.Model):
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog, null=True)
    name = models.CharField(verbose_name=_("Name"), max_length=140, null=True, blank=True)
    description = models.CharField(verbose_name=_("Description"), max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=140, unique=True)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    top_level_cat = models.ForeignKey('self',  null=True, blank=True)
    def __unicode__(self):
        return self.slug

class Tag(models.Model):
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog, null=True)
    name = models.CharField(verbose_name=_("Name"), max_length=140, null=True, blank=True)
    description = models.CharField(verbose_name=_("Description"), max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=140, unique=True)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    def __unicode__(self):
        return self.slug 

class Post(models.Model):
    author = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    base62id = models.CharField(max_length=140, blank=True)
    blog = models.ForeignKey(Blog, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
    status = models.CharField(max_length=2, choices=STATUS, default="P", null=True)
    translated_title = models.CharField(verbose_name=_("Titre traduit"), max_length=140, blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    karma = models.IntegerField(default=0)
    views = models.IntegerField(default=0, blank=True)
    source = models.URLField(verbose_name=_("Source"), max_length=300, blank=True)
    content = models.TextField(verbose_name=_("Contenu"),max_length=10000, blank=True)
    is_video = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)
    publish_on_facebook = models.BooleanField(default=False)
    youtube_id = models.CharField(max_length=50, null=True, blank=True)
    pic = ImageField(verbose_name=_("Image"), upload_to=get_file_path, null=True, blank=True)
    pic_0 = ImageField(verbose_name=_("Image_0"), upload_to=get_file_path_0, null=True, blank=True)
    pic_1 = ImageField(verbose_name=_("Image_1"), upload_to=get_file_path_1, null=True, blank=True)
    pic_2 = ImageField(verbose_name=_("Image_2"), upload_to=get_file_path_2, null=True, blank=True)
    pic_3 = ImageField(verbose_name=_("Image_3"), upload_to=get_file_path_3, null=True, blank=True)
    pic_4 = ImageField(verbose_name=_("Image_4"), upload_to=get_file_path_4, null=True, blank=True)
    pic_5 = ImageField(verbose_name=_("Image_5"), upload_to=get_file_path_5, null=True, blank=True)
    pic_6 = ImageField(verbose_name=_("Image_6"), upload_to=get_file_path_6, null=True, blank=True)
    pic_04 = ImageField(verbose_name=_("Image_04"), upload_to=get_file_path_7, null=True, blank=True)
    content_0 = models.TextField(verbose_name=_("Content_0"),max_length=10000, blank=True)
    content_01 = models.TextField(verbose_name=_("Content_01"),max_length=10000, blank=True)
    content_1 = models.TextField(verbose_name=_("Content_1"),max_length=10000, blank=True)
    content_2 = models.TextField(verbose_name=_("Content_2"),max_length=10000, blank=True)
    content_3 = models.TextField(verbose_name=_("Content_3"),max_length=10000, blank=True)
    content_4 = models.TextField(verbose_name=_("Content_4"),max_length=10000, blank=True)
    content_5 = models.TextField(verbose_name=_("Content_5"),max_length=10000, blank=True)
    content_6 = models.TextField(verbose_name=_("Content_6"),max_length=10000, blank=True)
    content_video = models.TextField(verbose_name=_("Content_video"),max_length=10000, blank=True)
    youtube_url = models.URLField(verbose_name=_("YoutubeURL"), max_length=300, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    artist = models.CharField(verbose_name=_("Artist"), max_length=140, blank=True)
    def __unicode__(self):
        return self.title

    def save(self):
        if not self.base62id:
            self.base62id = Post.generate_unique_id()
        return super(Post, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('blogs.views.single', [str(self.base62id)])

    @classmethod
    def generate_unique_id(cls):
        chars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
        id_exists = False
        while not id_exists:
            rnd_str=""
            for i in range(8):
                rnd_str = rnd_str + choice(chars)
            try:
                post = cls.objects.get(base62id=rnd_str)
                id_exists = True
            except cls.DoesNotExist:
                return rnd_str

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)
    blog = models.ForeignKey(Blog, null=True)
    comment = models.TextField(verbose_name=_("Content"),max_length=10000)
    email = models.EmailField(verbose_name=_("Email"))
    name = models.CharField(verbose_name=_("Name"), max_length=140)
    website = models.URLField(verbose_name=_("Website"), max_length=300, blank=True)
    notify_me = models.BooleanField(default=False)
    def __unicode__(self):
        return self.comment

#class Video(Post):
#    video_title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
#    content = models.TextField(verbose_name=_("Content"),max_length=10000, blank=True)
#    youtube_id = models.CharField(max_length=50, null=True, blank=True)
#    def __unicode__(self):
#        return str(self.id)
#
#class Album(Post):
#    title = models.CharField(verbose_name=_("Titre"), max_length=140)
#    content = models.TextField(verbose_name=_("Contenu"),max_length=10000, blank=True)
#    def __unicode__(self):
#        return str(self.id)
#
#class Link(models.Model):
#    image = models.ForeignKey(Image)
#    album = models.ForeignKey(Album)
#    order = models.PositiveIntegerField()
#    def __unicode__(self):
#        return str(self.id)
#
