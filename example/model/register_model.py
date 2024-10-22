from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class RegisterModel(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("O usuário ja´existe")
        return username