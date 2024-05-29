from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Car
 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username','email','first_name','last_name','password1','password2')
 
class LoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
   
   