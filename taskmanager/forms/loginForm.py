from django import forms

class Login_form(forms.Form):
    login = forms.CharField(label='Login', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
