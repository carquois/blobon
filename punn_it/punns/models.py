#!/usr/bin/env python
# -*- coding: utf-8 -*-

###IMPORTS###
#Django
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField, URLField, ModelForm, ModelMultipleChoiceField
from django.utils.translation import ugettext as _

#House
from punns.utils import BASE10, BASE62, baseconvert

#Others
import uuid
import os
from sorl.thumbnail import ImageField

STATUS = (
    ('P', 'Publish'),
    ('D', 'Draft'),
)

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    filename = "%s.%s" % (prefix, ext)
    return os.path.join('', filename)

class Tags(models.Model):
    tag = models.CharField(max_length=140)
    def __unicode__(self):
        return self.tag

class Punn(models.Model):
    status = models.CharField(max_length=2, choices=STATUS, null=True, blank=True)
    #Basic infos
    title = models.CharField(max_length=140)
    base62id = models.CharField(max_length=140, blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    karma = models.IntegerField(default=0)
    views = models.IntegerField(default=0, blank=True)
    source = models.URLField(max_length=300, blank=True)
    author = models.ForeignKey(User)
    original_punn = models.ForeignKey('self',  null=True, blank=True)
    content = models.TextField(max_length=10000, blank=True)
    is_video = models.BooleanField(default=False)
    youtube_id = models.CharField(max_length=50, null=True, blank=True)
    tags = models.ManyToManyField(Tags)
    #Datetime infos
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(null=True, blank=True)
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
    title = CharField(label=_('Title :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your title here')}))
    source = URLField(widget=forms.HiddenInput(), required=False)
    author = forms.ModelChoiceField(queryset=User.objects.all(), initial=User.objects.get(pk=3))
    status = forms.CharField(max_length=2, widget=forms.Select(choices=STATUS), initial='D')
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all())
    class Meta:
        model = Punn
        fields = ('title', 'author', 'status', 'tags')

