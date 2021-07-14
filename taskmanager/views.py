from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


from taskmanager.db.connector import UserManagement as User


class Homepage(View):
	def get(self, request):
		login = request.session["login"]
		res = {}
		
		data = User().getUsersTables(name=login)
		print(data)
		res["login"] = login
		ret = []
		for elem in data:
			ret.append(elem[1])

		print(ret)
		res["tables"] =  ret
		# return HttpResponse(f"Hello, world.-- {login}")
		return JsonResponse(res)