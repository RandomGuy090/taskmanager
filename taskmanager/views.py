from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from taskmanager.db.connector import UserManagement as User


class Homepage(View):
	def get(self, request):
		try:
			login = request.session["login"]
		except:
			return HttpResponseRedirect("/login")

		if login == None:
			return HttpResponseRedirect("/login")
		res = {}
		ret = []
		
		userInfo = User().getUserInfo(name=login)
		data = User().getUsersTables(name=login)
		print(data)
		res["login"] = login

		for elem in data:
			tmp = dict()
			tmp["name"] = elem[1]
			tmp["url"] = elem[2]
			tmp["color"] = elem[3]
			tmp["border"] = elem[4]
			ret.append(tmp)
			
		res["tables"] =  ret
		
		return render(request, "homepage.html", res)
