from django import forms

class Register_form(forms.Form):
    login = forms.CharField(label='_login', max_length=100)
    password1 = forms.CharField(label='_password1', max_length=100)
    password2 = forms.CharField(label='_password2', max_length=100)
