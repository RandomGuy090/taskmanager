from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import User_management as User
from taskmanager.forms.loginForm  import Login_form
from taskmanager.sec.secutils import Security as Sec

import bcrypt

class Login(View, Sec):
	def get(self, request, tableid=""):
		return render(request, "login.html", {
			"title": "log in"})
	
	def post(self, request, tableid=""):

		form = Login_form(request._post)
		
		if not form.is_valid():
			return render(request, "login.html", {
				"title": "log in",
				"error": "invalid login or password"})

		form.cleaned_data = self.make_safe(form.cleaned_data)
		login = form.cleaned_data["login"]
		password = form.cleaned_data["password"]
		password = password.encode()

		ret = User().get_password(name=login)
		if ret:
			ret = ret.encode()
		else:
			return render(request, "login.html", {
			"title": "log in",
			"error": "invalid login or password"})



		
		if bcrypt.checkpw(password, ret):	
			request.session["login"] = login
			if tableid  != "":
				return HttpResponseRedirect(f"/tables/{tableid}")

			return HttpResponseRedirect("/")


		return render(request, "login.html", {
			"title": "log in",
			"error": "invalid login or password"})

