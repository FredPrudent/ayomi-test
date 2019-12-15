from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Veuillez rentrer une adresse mail valide.')
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class UserUpdateForm (forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['email']
    