# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField
from django.utils.translation import ugettext as _

from posts.models import BlogPost

class BlogPostForm(ModelForm):
    title = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Title (optional)'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    content = CharField(widget=forms.Textarea(attrs={
                                                    'rows': '4',
                                                    'class': "form-control"}))

    class Meta:
        model = BlogPost 
        fields = ('title', 'content', 'status')

