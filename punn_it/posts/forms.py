# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField
from django.utils.translation import ugettext as _

from posts.models import Post

class PostForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Enter a title'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Say something clever'),
                                                    'rows': '4',
                                                    'class': "form-control"}))

    class Meta:
        model = Post
        fields = ('title', 'content', )

