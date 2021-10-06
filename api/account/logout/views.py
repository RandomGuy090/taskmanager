from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import  logout

class Logout(View):
	def get(self, request):
		try:
			logout(request)
			# return redirect("/")
			return JsonResponse({
				"status_code": 201,
				"detail": "logged out correctly",
			}) 
		except:
			return JsonResponse({
			"status_code": 401,
			"detail": "logout failed",
			}) 

