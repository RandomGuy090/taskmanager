from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from taskmanager.db.connector import UserManagement as User


class Homepage(View):
	def get(self, request):
		try:
			login = request.session["login"]
			print("login")
		except:
			return HttpResponseRedirect("/login")

		if login == None:
			return HttpResponseRedirect("/login")
		
		data = User().getUsersTables(name=login)
		res = {"name": login,
			"posts":data}
					
		
		return render(request, "homepage.html", res)
		
