from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from taskmanager.db.connector import UserManagement as User
from taskmanager.db.connector import TablesManagement as Tbl


@method_decorator(csrf_exempt, name='dispatch')
class Table(View):

	def post(self, request):
		user =  request.session["login"]
		if user == None:
			return JsonResponse({
				"success": False,
				"error": "login first"
				})

		vals = request.body.decode("utf-8")
		vals = json.loads(vals)
		name = vals["title"]
		color = vals["color"]
		password = vals["password"]

		print(f"name {name} color {color}")
		url = Tbl().createTable(name=name, color=color, 
			password=password, 
			user=user)

		return JsonResponse({"url":url})



