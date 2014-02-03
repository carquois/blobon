# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import UserProfile
from django.forms import ModelForm, Textarea, TextInput, CharField
from django.utils.translation import ugettext as _

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class SocialSignupForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'readonly' : True}))
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    avatar = forms.FileField(required=False)

class UserProfileForm(ModelForm):
    location = CharField(required=False, widget=forms.TextInput(attrs={
                                                    'type': 'text',
                                                    'class': "form-control"}))
    description = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Entrez une biographie'),
                                                    'rows': '4',
                                                    'class': "form-control"}))
    class Meta:
        model = UserProfile
        fields = ('description', 'avatar', 'location', )
        widgets = {
            'description': TextInput(attrs={'class': 'input-block-level'}),
            'location': TextInput(attrs={'class': 'input-block-level'}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  )
        widgets = {
            'username': TextInput(attrs={'type': 'text',
                                                    'class': "form-control"}),
            'first_name': TextInput(attrs={'type': 'text',
                                                    'class': "form-control"}),
            'last_name': TextInput(attrs={'type': 'text',
                                                    'class': "form-control"}),
        }
        labels = {
            'username': _("Nom d'utilisateur"),
            'pic': _('Image'),
        }

class Blobon_loginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Username'),
                                                    'type': 'text',
                                                    'class': "form-control",
                                                    'autofocus':'on',
                                                    'style': "max-width:220px;"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': _('Password'),
                                                    'class': "form-control",
                                                    'style': "max-width:220px;"}))








