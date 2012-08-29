#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import CharField, URLField, ModelForm
from punns.utils import BASE10, BASE62, baseconvert
from sorl.thumbnail import ImageField
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    filename = "%s.%s" % (prefix, ext)
    return os.path.join('', filename)

class Punn(models.Model):
    #Basic infos
    title = models.CharField(max_length=140)
    slug = models.CharField(max_length=140, blank=True)
    base62id = models.CharField(max_length=140, blank=True)
    karma = models.IntegerField(default=0)
    source = models.URLField(max_length=300, blank=True)
    author = models.ForeignKey(User)
    original_punn = models.ForeignKey('self',  null=True, blank=True)
    #Datetime infos
    #TODO make the pub_date into last_modified
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now = True,  null=True, blank=True)
    #Media
    pic = ImageField(upload_to=get_file_path, null=True, blank=True)
    def __unicode__(self):
        return self.title
    def save(self):
        super(Punn, self).save()
        if not self.base62id:
            self.base62id = baseconvert(str(self.id),BASE10,BASE62)
            self.save()
    @models.permalink
    def get_absolute_url(self):
        return ('punns.views.single', [str(self.base62id)])

class PunnForm(ModelForm):
    title = CharField()
    source = URLField(required=False)
    pic = ImageField()
    author = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Punn
        fields = ('title', 'author')

