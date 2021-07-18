from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import UserManagement as User
from taskmanager.db.connector import TablesManagement as Table

from taskmanager.forms.table_password_form  import Table_password



class Tables(View):
	def get(self, request, tableid=""):
		if tableid == "":
			# table not found
			return HttpResponseRedirect("/")

		info = Table().getTableInfo(url=tableid)[0]
		# userInfo = Table().listUsersTable(url=tableid)
		userInfo = Table().getTableColor(url=tableid)
		try:
			login =  request.session["login"]
		except:
			login = None;

	
		ret = {
		 	"users": userInfo,
		 	"login": login
		}

		
		if info["password"] == "":
			# no password needed
			print("passowrd not required")
			# no passed but add table to user
			if login != None:
				status = Table().addUserTable(user=login,url=info["url"])
				return render(request, "table_cal.html", ret)
			else:
			# bo passed and no user
				return render(request, "table_cal.html", ret)

		

		if login == None:
			# user not logged in and password needed
			return HttpResponseRedirect(f"/login/{tableid}")
		
		print("_----------------login")
		print(login)
		print(str(userInfo))

		if not login in str(userInfo):
			# user has to enter password
			return render(request, "table_pass.html" )
		# user logged in, password already entered

		return render(request, "table_cal.html", ret)
		

	
	def post(self, request, tableid):

		try:
			login = request.session["login"]
		except:
			return HttpResponseRedirect("/login")

		form = Table_password(request.POST)

		if not form.is_valid():
			#invalid password
			return render(request, "table_pass.html", {"error": "invalid password"})
		

		password = form.cleaned_data["password"]
		info = Table().getTableInfo(url=tableid)[0]
		
		if info["password"] == password:
			#password ok, adding user to table

			status = Table().addUserTable(user=login,url=info["url"])
		else:
			# password not ok, returning error
			return render(request, "table_pass.html", {"error": "invalid password"})

		# post ok password 
		return HttpResponseRedirect(f"/tables/{tableid}")





