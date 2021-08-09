from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from taskmanager.db.connector import User_management as User
from taskmanager.db.connector import Tables_management as Table
from taskmanager.db.connector import Tasks_management as Tsk

from taskmanager.sec.secutils import Security as Sec


@method_decorator(csrf_exempt, name='dispatch')
class Task(View, Sec):

	def post(self, request, tableid):
		login =  request.session["login"]
		user_info = Table().list_users_table(url=tableid)

		if login == None or not login in str(user_info):
			return JsonResponse({
				"success": False,
				"error": "login first"
				})


		vals = request.body.decode("utf-8")
		

		vals = json.loads(vals)
		
		vals = self.make_safe(vals)

		print(vals)
		

		time_start = vals["time_start"]
		time_end = vals["time_end"]
		day_start = vals["day_start"]
		day_end = vals["day_end"]
		task = vals["task"]
		
		if time_start == "" or 	\
			time_start == "" or \
			day_start == "" or 		\
			task == "":
			print("not enough data")
			return JsonResponse({
				"success": False,
				"error": "time input failure"
				})

		date_start = f"{day_start} {time_start}:00"
		date_end = f"{day_end} {time_end}:00"


		Tsk().create_task(date_start=date_start, date_end=date_end, \
							user=login, content=task, url=tableid)
	
		return JsonResponse({
				"success": True,
				"error": "processing"
				})


