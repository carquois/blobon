# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField
from django.utils.translation import ugettext as _

from punns.models import Punn

class SubmitForm(ModelForm):
    title = CharField(label=_('Title :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your title here.'), 'class': 'form-control'}))
    translated_title = CharField(label=_('Title translated :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your translation here.'), 'class': 'form-control'}), required=False)
    source = URLField(label=_('Source :'), widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Punn
        fields = ('title', 'translated_title', )

class PunnForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Entrez votre titre ici'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    source = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Entrez la source de votre contenu'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Entrez une description'),
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


