from django.http import  HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from taskmanager.forms.registerForm  import Register_form


from taskmanager.db.connector import User_management as User
from taskmanager.db.connector import Tables_management as Tbl
from taskmanager.sec.secutils import Security as Sec

import bcrypt 


class Register(View, Sec):
	def get(self, request, tableid=""):
		return render(request, "register.html", {
			"title": "register"})
	
	def post(self, request, tableid=""):

		form = Register_form(request._post)

		if not form.is_valid():
			return render(request, "register.html", {
				"title": "register",
				"error": "invalid login or password"})

		form.cleaned_data = self.make_safe(form.cleaned_data)

		login = form.cleaned_data["login"]
		password1 = form.cleaned_data["password1"]
		password2 = form.cleaned_data["password2"]
		

		
		if password2 != password1:
			return render(request, "register.html", {
				"title": "register",
				"error": "password's aren't same"})

		password = password1.encode()
		password = bcrypt.hashpw(password, bcrypt.gensalt())

		ret = User().create_user(name=login, password=password.decode("utf-8"))
		
		request.session["login"] = login
		if isinstance(ret, str):
			return render(request, "register.html", {
			"title": "log in",
			"error":ret})


		# return render(request, "register.html", {
		# 	"title": "log in"})
		return HttpResponseRedirect("/")

# <script>alert('xd')</script>