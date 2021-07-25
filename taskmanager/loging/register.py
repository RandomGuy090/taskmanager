from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import UserManagement as User
from taskmanager.forms.registerForm  import RegisterForm
from taskmanager.sec.secutils import Security as Sec

import bcrypt 


class Register(View, Sec):
	def get(self, request, tableid=""):
		return render(request, "register.html", {
			"title": "Register"})
	
	def post(self, request, tableid=""):

		form = RegisterForm(request.POST)

		if not form.is_valid():
			return render(request, "register.html", {
				"title": "Register",
				"error": "invalid login or password"})

		form.cleaned_data = self.makeSafe(form.cleaned_data)

		login = form.cleaned_data["login"]
		password1 = form.cleaned_data["password1"]
		password2 = form.cleaned_data["password2"]
		

		
		if password2 != password1:
			return render(request, "register.html", {
				"title": "Register",
				"error": "password's aren't same"})

		password = password1.encode()
		password = bcrypt.hashpw(password, bcrypt.gensalt())

		ret = User().createUser(name=login, password=password.decode("utf-8"))
		
		request.session["login"] = login
		if isinstance(ret, str):
			return render(request, "register.html", {
			"title": "Log in",
			"error":ret})


		# return render(request, "register.html", {
		# 	"title": "Log in"})
		return HttpResponseRedirect("/")

# <script>alert('xd')</script>