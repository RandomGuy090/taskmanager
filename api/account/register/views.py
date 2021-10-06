from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import  login


from .forms import RegisterForm

class Register(View):
	def get(self, request):
		form = RegisterForm(None)

		headers = {"title": "Register", "form":form}
		return render(request, "login.html", headers)


	def post(self, request):
		form = RegisterForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")

			login(request, form.user)

		else: 
			# headers = {"title": "Register", "form":form}
			return JsonResponse({
			"status_code": 401,
			"detail": "register failed",
			}) 
			# raise

		request.session["username"] = username
		return JsonResponse({
			"status_code": 201,
			"detail": "registered correctly",
			}) 
