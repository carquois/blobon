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
    pro_user = models.BooleanField(default=True)
    LANGUAGES_CHOICES = (
        ('en', 'English'),
        ('fr', 'Français'),
        ('qc', 'Québécois'),
    )
    language = models.CharField(default="en", max_length=2, choices=LANGUAGES_CHOICES)
    PUBLICATION_FREQUENCY_CHOICES = (
        ('15m', '15 minutes'),
        ('30m', '30 minutes'),
        ('1h', '1 hour'),
        ('3h', '3 hours'),
    )
    publication_frequency = models.CharField(default="30m", 
                                             max_length=3, 
                                             choices=PUBLICATION_FREQUENCY_CHOICES)
    is_obox_client = models.BooleanField(default=False, blank=True)
    #Google Infos
    analytics_account = models.CharField(max_length=50, blank=True)
    #Social media info
    facebook_link = models.URLField(max_length=100, blank=True)
    twitter_link = models.URLField(max_length=100, blank=True)
    def __unicode__(self):
        return self.description

class UserProfileForm(ModelForm):
    avatar   = ImageField(help_text="Maximum size of 700k. JPG, GIF, PNG.")
    location = CharField(help_text="Where in the world are you?")
    class Meta:
        model = UserProfile
        fields = ('avatar', 'domain')


