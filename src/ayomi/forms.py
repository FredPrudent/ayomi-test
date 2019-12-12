from django import forms
from.models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email