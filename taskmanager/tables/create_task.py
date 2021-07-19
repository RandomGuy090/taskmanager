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
		print(vals)
		# anti xss parsing
		vals = json.loads(vals)
		
		vals = self.antiXSS(vals)

		print(vals)


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



		Tsk().createTask(date=date, user=login, content=task, url=tableid)
	
		return JsonResponse({
				"success": True,
				"error": "processing"
				})


