from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .forms import LoginForm, RegisterForm

# Create your views here.

class Login(View):
	def get(self, request):
		form = LoginForm(None)

		headers = {"title": "Login", "form":form}
		# return ("login.html")
		return render(request, "login.html", headers)


	def post(self, request):
		form = LoginForm(request.POST or None)
		print(form)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			print(f"{username}:   {password}")
			login(request, form.user)

		else: 
			print("form invalid")
			headers = {"title": "Login", "form":form}
			return render(request, "login.html", headers)

		request.session["username"] = username
		return redirect("/")

class Register(View):
	def get(self, request):
		form = RegisterForm(None)

		headers = {"title": "Register", "form":form}
		return render(request, "login.html", headers)


	def post(self, request):
		form = RegisterForm(request.POST or None)
		print(form)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")

			print(f"{username}:   {password}")
			login(request, form.user)

		else: 
			print("form invalid")
			headers = {"title": "Register", "form":form}
			return render(request, "login.html", headers)
			
		request.session["username"] = username
		# return HttpResponse(username)
		return redirect("/")
