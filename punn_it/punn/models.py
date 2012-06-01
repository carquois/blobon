#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ImageField, EmailField, ModelForm, CharField, PasswordInput
from punn.utils import BASE10, BASE62, baseconvert

class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

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
    #Social infos
    image = models.URLField(max_length=300, blank=True)
    thumbnail = models.URLField(max_length=300, blank=True)
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



