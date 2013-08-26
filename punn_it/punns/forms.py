# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField
from django.utils.translation import ugettext as _

from punns.models import Punn

class PunnForm(ModelForm):
    class Meta:
        model = Punn
        fields = ('title', 'pic', 'source', 'content', 'publish_on_facebook', )
        widgets = {
            'title': TextInput(attrs={'class': 'input-block-level'}),
            'source': TextInput(attrs={'class': 'input-block-level'}),
            'content': Textarea(attrs={'class': 'input-block-level'}),
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


