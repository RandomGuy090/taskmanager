from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from taskmanager.db.connector import UserManagement as User
from taskmanager.db.connector import TablesManagement as Table
from taskmanager.db.connector import TasksManagement as Tsk


@method_decorator(csrf_exempt, name='dispatch')
class Task(View):

	def post(self, request, tableid):
		login =  request.session["login"]
		userInfo = Table().listUsersTable(url=tableid)

		if login == None or not login in str(userInfo):
			return JsonResponse({
				"success": False,
				"error": "login first"
				})


		vals = request.body.decode("utf-8")
		vals = json.loads(vals)

		time = vals["time"]
		day = vals["day"]
		task = vals["task"]
		date = f"{day} {time}:00"
		if time == "" or day == "" or task == "":
			print("not enough data")
			return JsonResponse({
				"success": False,
				"error": "time input failure"
				})



		print(vals)
		Tsk().createTask(date=date, user=login, content=task, url=tableid)
	
		return JsonResponse({
				"success": True,
				"error": "processing"
				})


