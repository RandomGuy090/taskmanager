from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth import authenticate, logout, login, get_user_model


from .forms import RegisterForm
User = get_user_model()


class Register(View):
	def get(self, request):
		form = RegisterForm(None)

		headers = {"title": "Register", "form":form}
		return render(request, "login.html", headers)


	def post(self, request):
		data = self.request.body
		data = data.decode("utf-8")
		data = json.loads(data)

		username = data.get("username")
		password = data.get("password")
		password2 = data.get("password2")

		print(username, password, password2)
		if password2 != password:
			print("password does not match")
			return JsonResponse({
				"status_code": 403,
				"detail": "passwords does not match",
				})

		qr = User.objects.filter(username=username)
		if qr.exists():
			print("user already exists")
			return JsonResponse({
				"status_code": 403,
				"detail": "user already exists",
				})
		user = User.objects.create_user(username=username, password=password)
		user.save()
		user = authenticate(username=username, password=password)

		login(request, user)

		request.session["username"] = username
		return JsonResponse({
			"status_code": 201,
			"detail": "registered correctly",
			}) 
