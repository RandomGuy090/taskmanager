from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login


class Tables(View):
	http_method_names = ['get']

	def get(self, request, table_id=""):
		username = request.session.get("username")
		# return render(request, "login.html", headers)
		return HttpResponse(f"tables - {username}, id = {table_id}")


