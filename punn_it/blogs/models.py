#!/usr/bin/env python
# -*- coding: utf-8 -*-

###IMPORTS###
#Django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from sorl.thumbnail import ImageField

STATUS = (
    ('Pu', 'Public'),
    ('Pr', 'Private'),
)

class Blog(models.Model):
    creator = models.ForeignKey(User, null=True)
    status = models.CharField(max_length=2, choices=STATUS)
    slug = models.SlugField(verbose_name=_("URL"), max_length=30, unique=True)
    title = models.CharField(verbose_name=_("Title"), max_length=140)
    password = models.CharField(verbose_name=_("Password"), max_length=140, blank=True)
    def __unicode__(self):
        return self.title
    
