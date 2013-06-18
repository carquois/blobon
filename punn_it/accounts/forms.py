from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile
from django.forms import ModelForm, TextInput

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
    class Meta:
        model = UserProfile
        fields = ('description', 'avatar', )
        widgets = {
            'description': TextInput(attrs={'class': 'input-block-level'}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )
        widgets = {
            'username': TextInput(attrs={'class': 'input-block-level'}),
            'first_name': TextInput(attrs={'class': 'input-block-level'}),
            'last_name': TextInput(attrs={'class': 'input-block-level'}),
        }



