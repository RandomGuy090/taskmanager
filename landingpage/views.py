from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login


class LandingPage(View):
	def get(self, request):
		username = request.session.get("username")
		# return render(request, "login.html", headers)
		return HttpResponse(username)


