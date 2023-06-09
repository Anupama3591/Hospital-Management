from django import forms
from . models import User1

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.models import User

class PatientRegistraion(forms.ModelForm):
    class Meta:
        model=User1
        fields="__all__"
        # widgets = {'name': forms.TextInput(attrs={'class':'form-control'}),'phonenumber': forms.IntegerField(attrs={'class':'form-control'}),'gender': forms.TextInput( attrs={'class':'form-control'}),'fee':forms.IntegerField(attrs={'class':"form-control"}),'Condition':forms.TextInput(attrs={'class':'form-control'}) }
class SignUpForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
  'first_name':forms.TextInput(attrs={'class':'form-control'}),
  'last_name':forms.TextInput(attrs={'class':'form-control'}),
  'email':forms.EmailInput(attrs={'class':'form-control'}),
  }

class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
 password = forms.CharField(label=_("Password"),  widget=forms.PasswordInput(attrs={'class':'form-control'}))