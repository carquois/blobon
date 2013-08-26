# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField
from django.utils.translation import ugettext as _

from punns.models import Punn

class PunnForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Entrez votre titre ici'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    source = CharField(widget=forms.TextInput(attrs={'placeholder': _('Entrez la source de votre contenu'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    content = CharField(widget=forms.Textarea(attrs={'placeholder': _('Entrez une description'),
                                                    'rows': '4',
                                                    'class': "form-control"}))
    class Meta:
        model = Punn
        fields = ('title', 'pic', 'source', 'content', )

        labels = {
            'title': _('Titre'),
            'pic': _('Image'),
            'content': _('Description'),
        }

class QuickPublish(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Entrez votre titre ici'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    class Meta:
        model = Punn
        fields = ('title', 'pic')
        labels = {
            'title': _('Titre'),
            'pic': _('Image'),
        }
        help_texts = {
            'title': _('Entrez un titre'),
        }


