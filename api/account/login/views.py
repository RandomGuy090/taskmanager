from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login

from rest_framework.response import Response

from .forms import LoginForm

from taskmanager.exceptions import LoginOK


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
			data = form.errors.as_json()
			data = json.loads(data)
			data = data["__all__"][0]
			return JsonResponse(data) 

		request.session["username"] = username
		return JsonResponse({
			"status_code": 201,
			"detail": "logged correctly",
			}) 