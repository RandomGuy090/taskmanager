from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import User_management as User
from taskmanager.db.connector import Tables_management as Table

from taskmanager.forms.table_password_form  import Table_password

import bcrypt

class Tables(View):
	def get(self, request, tableid=""):
		if tableid == "":
			# table not found
			return HttpResponseRedirect("/")
		print("get_table_info")
		try:
			info = Table().get_table_info(url=tableid)[0]
		except:
			# return _HttpResponse("no such table")
			return render(request, "no_such_table.html")
			
		# user_info = Table().list_users_table(url=tableid)
		print("user_info")
		user_info = Table().get_table_color(url=tableid)
		try:
			login =  request.session["login"]
		except:
			login = None;

	
		ret = {
		 	"users": user_info,
		 	"login": login
		}

		
		if info["password"] == "":
			# no passed but add table to user
			if login != None:
				status = Table().add_user_table(user=login,url=info["url"])
				return render(request, "table_cal.html", ret)
			else:
			# bo passed and no user
				return render(request, "table_cal.html", ret)

		

		if login == None:
			# user not logged in and password needed
			return HttpResponseRedirect(f"/login/{tableid}")
		if not login in str(user_info):
			# user has to enter password
			return render(request, "table_pass.html" )
		# user logged in, password already entered

		return render(request, "table_cal.html", ret)
		

	
	def post(self, request, tableid):

		try:
			login = request.session["login"]
		except:
			return HttpResponseRedirect("/login")

		form = Table_password(request._post)

		if not form.is_valid():
			#invalid password
			return render(request, "table_pass.html", {"error": "invalid password"})
		

		password = form.cleaned_data["password"]
		info = Table().get_table_info(url=tableid)[0]
		
		if bcrypt.checkpw(password.encode(),info["password"].encode()):
			#password ok, adding user to table

			status = Table().add_user_table(user=login,url=info["url"])
		else:
			# password not ok, returning error
			return render(request, "table_pass.html", {"error": "invalid password"})

		# post ok password 
		return HttpResponseRedirect(f"/tables/{tableid}")





