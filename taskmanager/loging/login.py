from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import UserManagement as User
from taskmanager.forms.loginForm  import LoginForm
from taskmanager.sec.secutils import Security as Sec

import bcrypt

class Login(View, Sec):
	def get(self, request, tableid=""):
		return render(request, "login.html", {
			"title": "Log in"})
	
	def post(self, request, tableid=""):

		form = LoginForm(request.POST)
		
		if not form.is_valid():
			return render(request, "login.html", {
				"title": "Log in",
				"error": "invalid login or password"})

		form.cleaned_data = self.makeSafe(form.cleaned_data)
		login = form.cleaned_data["login"]
		password = form.cleaned_data["password"]
		password = password.encode()

		ret = User().getPassword(name=login).encode()
		
		if bcrypt.checkpw(password, ret):	
			request.session["login"] = login
			if tableid  != "":
				return HttpResponseRedirect(f"/tables/{tableid}")

			return HttpResponseRedirect("/")


		return render(request, "login.html", {
			"title": "Log in",
			"error": "invalid login or password"})

