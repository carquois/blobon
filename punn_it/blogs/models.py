#!/usr/bin/env python
# -*- coding: utf-8 -*-

###IMPORTS###
#Django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from sorl.thumbnail import ImageField

PRIVACY = (
    ('Pu', 'Public'),
    ('Pr', 'Private'),
)

STATUS = (
    ('P', 'Publish'),
    ('D', 'Draft'),
)

class Blog(models.Model):
    creator = models.ForeignKey(User, null=True)
    is_open = models.BooleanField(default=False)
    slug = models.SlugField(verbose_name=_("URL"), max_length=30, unique=True)
    title = models.CharField(verbose_name=_("Title"), max_length=140)
    password = models.CharField(verbose_name=_("Password"), max_length=140, blank=True)
    def __unicode__(self):
        return self.title

#class Page(models.Model):
#    blog = models.ForeignKey(Blog, null=True)
#    author = models.ForeignKey(User, null=True)
#    status = models.CharField(max_length=2, choices=STATUS)
#    title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
#    content = models.TextField(verbose_name=_("Content"),max_length=10000, blank=True)
#    created = models.DateTimeField(auto_now_add = True)
#    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
#    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
#    def __unicode__(self):
#        return self.title


#class Category(models.Model):
#    author = models.ForeignKey(User)
#    blog = models.ForeignKey(Blog, null=True)
#    name = models.CharField(verbose_name=_("Name"), max_length=140)
#    description = models.CharField(verbose_name=_("Description"), max_length=1000)
#    slug = models.SlugField(max_length=140, unique=True)
#    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
#    top_level_cat = models.ForeignKey('self',  null=True, blank=True)
#    def __unicode__(self):
#        return self.slug
#
#class Tag(models.Model):
#    author = models.ForeignKey(User)
#    blog = models.ForeignKey(Blog, null=True)
#    name = models.CharField(verbose_name=_("Name"), max_length=140)
#    description = models.CharField(verbose_name=_("Description"), max_length=1000)
#    slug = models.SlugField(max_length=140, unique=True)
#    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
#    def __unicode__(self):
#        return self.slug 
