from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()   # you can pass reuqired=false if you want
    
    class Meta:
        # we neeed to tell which Model you should interact when submitting this form
        model = User  

        # we neeed to tell which fields we want to shown
        fields = ['username', 'email', 'password1', 'password2']