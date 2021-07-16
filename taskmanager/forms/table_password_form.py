from django import forms

class Table_password(forms.Form):
    password = forms.CharField(label='Password', max_length=100)
