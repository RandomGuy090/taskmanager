from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, logout, login, get_user_model

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json


from taskmanager.exceptions import (
	NotLogged
	)


User = get_user_model()

@method_decorator(csrf_exempt, name='dispatch')
class Token(View):


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