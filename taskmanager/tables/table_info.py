from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from taskmanager.db.connector import TasksManagement as Task
from taskmanager.db.connector import TablesManagement as Table

import json

@method_decorator(csrf_exempt, name='dispatch')
class Info(View):
	def post(self, request, tableid=""):
		# if tableid == "":
		# 	# table not found
		# 	return JsonResponse({
		# 		"success": False,
		# 		"error": "table id not found"
		# 		})

		try:
			login = request.session["login"]
		except:
			login = None;

		info = Table().getTableInfo(url=tableid)[0]
		users = Table().listUsersTable(url=tableid)


		# if login == None and info["password"] != "":
		# 	return JsonResponse({
		# 		"success": False,
		# 		"error": "join table first"
		# 		})

		# if not login in str(users):
		# 	# user has to enter password

		# 	return JsonResponse({
		# 		"success": False,
		# 		"error": "join table first"
		# 		})

		vals = request.body
		vals = json.loads(vals)
		print(vals)
		day = vals["day"] if "day" in vals else False
		month = vals["month"] if "month" in vals else False
		year = vals["year"] if "year" in vals else False
		url = vals["url"] if "url" in vals else False
		if url != tableid:
			return JsonResponse({
				"success": False,
				"error": "bad table id"
				})
		if year and url and day:
			tasks = Task().getDay(year=year, month=month, day=day, url=url)
					
		elif year and month and day == False:
			tasks = Task().getMonth(month=month, year=year, url=url)
		
		elif year and month == False and day == False:
			tasks = Task().getYear(year=year, url=url)
		
		else:
			tasks = {
			"status": False,
			"error": "not enough data"
			}



		print(f"""{day} {month} {year} {url}""")
		print({	"tasks": tasks	})

		return JsonResponse({
			"tasks": tasks
			})

		
		

	
