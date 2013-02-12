#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django import forms
from django.forms import ImageField, EmailField, ModelForm, CharField, PasswordInput

from social_auth.signals import socialauth_registered


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
    
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(blank=True, max_length=100, null=True, choices=(('m', 'Male'), ('f', 'Female'),))
    fb_friends = models.TextField(blank=True, null=True)
    fb_likes = models.TextField(blank=True, null=True)
    fb_avatar = models.ImageField(upload_to='pics', blank=True, null=True)
    is_new_from_social = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.description

class UserProfileForm(ModelForm):
    avatar   = ImageField(help_text="Maximum size of 700k. JPG, GIF, PNG.")
    location = CharField(help_text="Where in the world are you?")
    class Meta:
        model = UserProfile
        fields = ('avatar', 'domain')



def create_user_profile(sender, instance, created, **kwargs):
    """Add a signal to make sure a user profile is created for all users"""
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


def new_users_handler(sender, user, response, details, **kwargs):
    """
    When a user is created from a social authentification (facebook, twitter or google)
    we mark it inactive so the signup proces can continue
    """
    profile = user.get_profile()
    profile.is_new_from_social = True
    profile.save()

socialauth_registered.connect(new_users_handler, sender=None)

