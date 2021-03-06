from django import forms
from django.contrib.auth import get_user_model, authenticate, login
User = get_user_model()

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		if self.password != self.password2:
			raise forms.ValidationError("passwords are not equal!")

		qs = User.objects.filter(username=self.username)		
		
		user = authenticate(username=self.username, password=self.password)
		if qs.exists():
			raise forms.ValidationError("Such user already exists")

		user = User.objects.create_user(username=self.username, password=self.password)
		user.save()

		self.user = user


	def clean_username(self):
		self.username = self.cleaned_data.get("username")	
		return self.username


	def clean_password(self):
		self.password = self.cleaned_data.get("password")
		return self.password

	def clean_password2(self):
		self.password2 = self.cleaned_data.get("password2")
		return self.password2

