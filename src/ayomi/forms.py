from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):
    
    class Meta:
        model = User
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'form-input'}),
        }
        fields = ['username','email', 'password1', 'password2']
    

class UserUpdateForm (forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['email']
    