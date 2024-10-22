from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=1)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(min_length=8)
    password2 = forms.CharField(min_length=8)