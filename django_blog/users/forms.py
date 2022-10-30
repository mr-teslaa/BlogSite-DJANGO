from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()   # you can pass reuqired=false if you want
    
    class Meta:
        # we neeed to tell which Model you should interact when submitting this form
        model = User  

        # we neeed to tell which fields we want to shown
        fields = ['username', 'email', 'password1', 'password2']


# we need to use ModelForm to update any database related form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()   # you can pass reuqired=false if you want
    
    class Meta:
        model = User  
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']