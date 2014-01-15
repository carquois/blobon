# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField
from django.utils.translation import ugettext as _

from blogs.models import Blog, Post

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
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Write your title here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write a new post'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_0 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_01 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_1 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_2 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_3 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_4 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_5 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_6 = CharField(widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    class Meta:
        model = Post 
        fields = ('title','content','content_1','content_2','content_3','content_4','content_5','content_6', 'pic', 'pic_1','pic_2','pic_3','pic_4','pic_5','pic_6', )
