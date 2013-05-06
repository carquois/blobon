from django import forms
from django.forms import ModelForm

from punns.models import Punn

class PunnForm(ModelForm):
    class Meta:
        model = Punn
        fields = ('title', 'pic', 'source', 'content', 'tags', )
