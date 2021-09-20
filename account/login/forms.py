from django import forms
from django.contrib.auth import get_user_model, authenticate, login
User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		user = authenticate(username=self.username, password=self.password)
		print(user)
		if user is None:
			raise forms.ValidationError("This is a invalid user.")
		self.user = user


	def clean_username(self):
		self.username = self.cleaned_data.get("username")	
		return self.username


	def clean_password(self):
		self.password = self.cleaned_data.get("password")
		return self.password