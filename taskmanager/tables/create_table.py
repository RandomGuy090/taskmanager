from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from taskmanager.db.connector import UserManagement as User
from taskmanager.db.connector import TablesManagement as Tbl
from taskmanager.sec.secutils import Security as Sec

import bcrypt

@method_decorator(csrf_exempt, name='dispatch')
class Table(View, Sec):

	def post(self, request):
		user =  request.session["login"]
		if user == None:
			return JsonResponse({
				"success": False,
				"error": "login first"
				})

		vals = request.body.decode("utf-8")
		vals = json.loads(vals)
		
		vals = self.makeSafe(vals)

		name = vals["title"]
		color = vals["color"]
		password = vals["password"]
		password = password.encode()
		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		hashed = hashed.decode("utf-8")

		print(f"name {name} color {color}")
		url = Tbl().createTable(name=name, color=color, 
			password=hashed, 
			user=user)

		return JsonResponse({"url":url})

	def changeBlackColor(self, color):
		color = color[1:]
		color = int(color[:2],16),int(color[2:4],16), int(color[4:],16)
		if color[0] == color[1] and color[0] == color[2]:
			if color[0] < 70:
				color = "#656565"
				return color



