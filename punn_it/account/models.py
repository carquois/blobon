#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.forms import ImageField, EmailField, ModelForm, CharField, PasswordInput
from django import forms


class UserForm(ModelForm):
    username = CharField(help_text="Don't worry, you can change it later.")
    email = EmailField(help_text="What's your email address?")
    password = CharField(help_text="Be tricky.",widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #Basic infos
    description = models.CharField(max_length=160, blank=True)
    avatar = models.ImageField(upload_to='pics', blank=True)
    domain = models.URLField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    sites = models.ForeignKey(Site, blank=True, null=True)
    LANGUAGES_CHOICES = (
        ('en', 'English'),
        ('fr', 'Francais'),
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

class UserProfileForm(ModelForm):
    avatar   = ImageField(help_text="Maximum size of 700k. JPG, GIF, PNG.")
    location = CharField(help_text="Where in the world are you?")
    class Meta:
        model = UserProfile
        fields = ('avatar', 'domain')


