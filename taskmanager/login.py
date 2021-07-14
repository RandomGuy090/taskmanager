from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import UserManagement as User
from taskmanager.forms.loginForm  import LoginForm

class Login(View):
	def get(self, request):
		return render(request, "login.html", {
			"title": "Log in"})
	
	def post(self, request):
		form = LoginForm(request.POST)
		print(form.is_valid())

		if not form.is_valid():
			return HttpResponseRedirect("/login")

		login = form.cleaned_data["login"]
		password = form.cleaned_data["password"]

		ret = User().getPassword(name=login)
		if ret == password:	
			request.session["login"] = login
			return HttpResponseRedirect("/")


		return render(request, "login.html", {
			"title": "Log in",
			"error": "invalid login or password"})

