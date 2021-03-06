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
from random import choice
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

class Cat(models.Model):
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=140, unique=True)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    is_top_level = models.BooleanField(default=False)
    top_level_cat = models.ForeignKey('self',  null=True, blank=True)
    def __unicode__(self):
        return self.slug
    @models.permalink
    def get_absolute_url(self):
        return ('punns.views.cat', [str(self.slug)])

class Punn(models.Model):
    status = models.CharField(max_length=2, choices=STATUS, null=True, blank=True)
    #Basic infos
    title = models.CharField(verbose_name=_("Titre"), max_length=140, blank=True)
    translated_title = models.CharField(verbose_name=_("Titre traduit"), max_length=140, blank=True)
    base62id = models.CharField(max_length=140, blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    karma = models.IntegerField(default=0)
    views = models.IntegerField(default=0, blank=True)
    source = models.URLField(verbose_name=_("Source"), max_length=300, blank=True)
    author = models.ForeignKey(User)
    cat = models.ForeignKey(Cat,  null=True, blank=True)
    original_punn = models.ForeignKey('self',  null=True, blank=True)
    content = models.TextField(verbose_name=_("Contenu"),max_length=10000, blank=True)
    is_video = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)
    publish_on_facebook = models.BooleanField(default=False)
    youtube_id = models.CharField(max_length=50, null=True, blank=True)
    tags = models.ManyToManyField(Tags,  null=True, blank=True)
    #Datetime infos
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    #Media
    pic = ImageField(verbose_name=_("Image"), upload_to=get_file_path, null=True, blank=True)
    def __unicode__(self):
        return self.title
    
    def save(self):
        if not self.base62id:
            self.base62id = Punn.generate_unique_id()

        return super(Punn, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('punns.views.single', [str(self.base62id)])

    @classmethod
    def generate_unique_id(cls):
        chars = ('abcdefghijklmnopqrstuvwxyz1234567890')
        id_exists = False
        while not id_exists:
            rnd_str=""
            for i in range(8):
                rnd_str = rnd_str + choice(chars)
            try:
                punn = cls.objects.get(base62id=rnd_str)
                id_exists = True
            except cls.DoesNotExist:
                return rnd_str

class Album(models.Model):
    base62id = models.CharField(max_length=140, blank=True)
    title = models.CharField(verbose_name=_("Titre"), max_length=140)
    content = models.TextField(verbose_name=_("Contenu"),max_length=10000, blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add = True, null=True)
    last_modified_date = models.DateTimeField(auto_now = True,  null=True, blank=True)
    def __unicode__(self):
        return str(self.id)

    def save(self):
        if not self.base62id:
            self.base62id = Album.generate_unique_id()
        return super(Album, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('punns.views.album', [str(self.base62id)])

    @classmethod
    def generate_unique_id(cls):
        chars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
        id_exists = False
        while not id_exists:
            rnd_str=""
            for i in range(8):
                rnd_str = rnd_str + choice(chars)
            try:
                album = cls.objects.get(base62id=rnd_str)
                id_exists = True
            except cls.DoesNotExist:
                return rnd_str

class Link(models.Model):
    punn = models.ForeignKey(Punn)
    album = models.ForeignKey(Album)
    order = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add = True, null=True)
    last_modified_date = models.DateTimeField(auto_now = True,  null=True, blank=True)
    def __unicode__(self):
        return str(self.id)

class Reblog(models.Model):
    author = models.ForeignKey(User)
    origin = models.ForeignKey(Punn)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)

class Favorite(models.Model):
    author = models.ForeignKey(User)
    punn = models.ForeignKey(Punn)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)

class CatForm(ModelForm):
    slug = CharField(label=_('Category :'), widget=forms.TextInput(attrs={'placeholder': _('Enter the category here.'),
                                                                          'type': 'text',
                                                                          'class': 'form-control', }))
    class Meta:
        model = Cat 
        fields = ('slug',)

class LinkForm(ModelForm):
    class Meta:
        model = Link 
        fields = ['album', 'punn', 'order', ]

class AlbumForm(ModelForm):
    title = CharField(label=_('Titre :'), widget=forms.TextInput(attrs={'placeholder': _('Entrez votre titre ici'),
                                                                          'type': 'text',
                                                                          'class': 'form-control', }))
    class Meta:
        model = Album 
        fields = ('title', )


class PunnForm(ModelForm):
    title = CharField(label=_('Title :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your title here.'), 'class': 'form-control'}))
    source = URLField(label=_('Source :'), widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Punn
        fields = ('title', )

