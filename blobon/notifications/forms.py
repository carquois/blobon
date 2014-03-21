from django import forms
from django.forms import ModelForm, EmailField
from django.utils.translation import ugettext as _

from notifications.models import Invitation 

class InvitationForm(ModelForm):
     email = EmailField(widget=forms.TextInput(attrs={'placeholder': _('Enter your email to request an invitation'),
                                                    'class': "form-control"}))
     class Meta:
        model = Invitation 
        labels = {
            'email': _('Email'),
        }
