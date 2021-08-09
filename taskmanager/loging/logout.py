
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render


class Logout(View):
	def get(self, request):
		return self.post(request)

	def post(self, request):
		request.session["login"] = None
		return HttpResponseRedirect("/")
