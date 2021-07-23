from django import forms

class RegisterForm(forms.Form):
    login = forms.CharField(label='Login', max_length=100)
    password1 = forms.CharField(label='Password1', max_length=100)
    password2 = forms.CharField(label='Password2', max_length=100)
