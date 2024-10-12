from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=1)
    senha = forms.CharField(min_length=8)