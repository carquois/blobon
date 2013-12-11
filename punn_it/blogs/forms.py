# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField
from django.utils.translation import ugettext as _

from blogs.models import Blog

class BlogForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Enter your title'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog adress'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    class Meta:
        model = Blog 
        fields = ('title', 'slug', 'status', )

