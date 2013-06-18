from django import forms
from django.forms import ModelForm, Textarea, TextInput

from punns.models import Punn

class PunnForm(ModelForm):
    class Meta:
        model = Punn
        fields = ('title', 'pic', 'source', 'content', )
        widgets = {
            'title': TextInput(attrs={'class': 'input-block-level'}),
            'source': TextInput(attrs={'class': 'input-block-level'}),
            'content': Textarea(attrs={'class': 'input-block-level'}),
        }


