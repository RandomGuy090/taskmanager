from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, logout, login, get_user_model

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
from django.contrib.auth import login

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from taskmanager.exceptions import (
	NotLogged
	)


User = get_user_model()


# class MyBasicAuthentication(BasicAuthentication):

#     def authenticate(self, request):
#         user, _ = super(MyBasicAuthentication, self).authenticate(request)
#         login(request, user)
#         return user, _

# @method_decorator(csrf_exempt, name='dispatch')
# class Login(APIView):
#     authentication_classes = (SessionAuthentication,)


#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
	authentication_classes = (SessionAuthentication)
	# permission_classes = (IsAuthenticated,)



	def post(self, request):
		data = self.request.body
		data = data.decode("utf-8")
		data = json.loads(data)
		self.request.session["username"] = "chuj"


		username = data.get("username")
		user = User.objects.filter(username=username)
		password = data.get("password")
		user = authenticate(username=username, password=password)
		print(user)
		if user != None:
			login(self.request, user)
			self.request.session["username"] = username
			print(self.request.user.is_authenticated)
			print(self.request.user.is_authenticated)
			print(self.request.user)
			print(self.request.session.items())

			return JsonResponse({
				"status_code": 201,
				"detail": "logged correctly",
				})
		else:
			return JsonResponse({
				"status_code": 403,
				"detail": "login failed",
				}) 