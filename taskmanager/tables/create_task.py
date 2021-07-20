from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from taskmanager.db.connector import UserManagement as User
from taskmanager.db.connector import TablesManagement as Table
from taskmanager.db.connector import TasksManagement as Tsk

from taskmanager.sec.secutils import Security as Sec


@method_decorator(csrf_exempt, name='dispatch')
class Task(View, Sec):

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
		
		vals = self.makeSafe(vals)

		print(vals)
		

		time_start = vals["time_start"]
		time_end = vals["time_end"]
		day = vals["day"]
		task = vals["task"]
		
		if time_start == "" or 	\
			time_start == "" or \
			day == "" or 		\
			task == "":
			print("not enough data")
			return JsonResponse({
				"success": False,
				"error": "time input failure"
				})

		date_start = f"{day} {time_start}:00"
		date_end = f"{day} {time_end}:00"


		Tsk().createTask(date_start=date_start, date_end=date_end, user=login, content=task, url=tableid)
	
		return JsonResponse({
				"success": True,
				"error": "processing"
				})


