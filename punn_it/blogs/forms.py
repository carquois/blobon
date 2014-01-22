# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField
from django.utils.translation import ugettext as _

from blogs.models import Blog, Post, Category

class BlogForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Enter your title'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog adress'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    class Meta:
        model = Blog 
        fields = ('title', 'slug', )

class SubmitForm(ModelForm):
    title = CharField(label=_('Title :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your title here.'), 'class': 'form-control'}), required=False)
    translated_title = CharField(label=_('Title translated :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your translation here.'), 'class': 'form-control'}), required=False)
    source = URLField(label=_('Source :'), widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Post
        fields = ('title', 'translated_title',)

class SettingsForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog title'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog adress'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    password = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog password'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    custom_domain = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your custom domain'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    description = CharField(widget=forms.Textarea(attrs={'placeholder': _('Describe Your Blog'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level"}))    
    class Meta:
        model = Blog 
        fields = ('title', 'slug', 'password', 'custom_domain', )

class PostForm(ModelForm):
    title = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write your title here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    source = URLField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your source'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    artist = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write artist name here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write a new post'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_0 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_01 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_1 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_2 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_3 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_4 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_5 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_6 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_video = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this video'),
                                                    'type': 'text',
                                                    'rows': '3',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    youtube_url = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Copy a Youtube url here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    class Meta:
        model = Post 
        fields = ('title','content','artist','content_0','content_01','content_1','content_2','content_3','content_4','content_5','content_6','content_video', 'pic','pic_0','pic_04','pic_1','pic_2','pic_3','pic_4','pic_5','pic_6','youtube_url','category', )
