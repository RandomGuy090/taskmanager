from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from taskmanager.db.connector import User_management as User


class Homepage(View):
	def get(self, request):
		try:
			login = request.session["login"]
		except:
			return HttpResponseRedirect("/login")

		if login == None:
			return HttpResponseRedirect("/login")
		
		data = User().get_users_tables(name=login)
		res = {"name": login,
			"posts":data}
		
		return render(request, "homepage.html", res)
		