from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, logout, login, get_user_model

from rest_framework.response import Response

from .forms import LoginForm
import json
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator


from taskmanager.exceptions import (
	NotLogged
	)

from rest_framework import permissions

User = get_user_model()
class Login(View):


	def post(self, request):
		data = self.request.body
		data = data.decode("utf-8")
		data = json.loads(data)

		username = data.get("username")
		user = User.objects.filter(username=username)
		password = data.get("password")
		user = authenticate(username=username, password=password)
		if user != None:
			login(request, user)
			request.session["username"] = username
			return JsonResponse({
				"status_code": 201,
				"detail": "logged correctly",
				})
		else:
			return JsonResponse({
				"status_code": 403,
				"detail": "login failed",
				}) 