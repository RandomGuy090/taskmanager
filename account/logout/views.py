from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from django.contrib.auth import  logout

class Logout(View):
	def get(self, request):
		print("logout")
		logout(request)
		return redirect("/")

