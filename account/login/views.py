from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login


from .forms import LoginForm


class Login(View):
	def get(self, request):
		form = LoginForm(None)

		headers = {"title": "Login", "form":form}
		# return ("login.html")
		return render(request, "login.html", headers)


	def post(self, request):
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			login(request, form.user)

		else: 
			headers = {"title": "Login", "form":form}
			return render(request, "login.html", headers)

		request.session["username"] = username
		return redirect("/")