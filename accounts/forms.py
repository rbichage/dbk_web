from django.contrib.auth.forms import UserCreationForm

from accounts.models import Donor
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Donor
        fields = {'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password'
                  }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
