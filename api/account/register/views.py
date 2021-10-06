from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
import json

from django.contrib.auth import  login


from .forms import RegisterForm

class Register(View):
	def get(self, request):
		form = RegisterForm(None)

		headers = {"title": "Register", "form":form}
		return render(request, "login.html", headers)


	def post(self, request):
		form = RegisterForm(request.POST or None)
		username = request.POST.get("username")
		password = request.POST.get("password")
		password2 = request.POST.get("password2")

		print(username, password, password2)

		if form.is_valid():

			login(request, form.user)

		else: 
			# headers = {"title": "Register", "form":form}
			# return JsonResponse({
			# "status_code": 401,
			# "detail": "register failed",
			# }) 
			# # raise
			data = form.errors.as_json()
			data = json.loads(data)
			data = data["__all__"][0]
			return JsonResponse(data) 

		request.session["username"] = username
		return JsonResponse({
			"status_code": 201,
			"detail": "registered correctly",
			}) 
