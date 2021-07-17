from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import UserManagement as User
from taskmanager.db.connector import TablesManagement as Table

from taskmanager.forms.table_password_form  import Table_password



class Tables(View):
	def get(self, request, tableid):
		info = Table().getTableInfo(url=tableid)[0]
		if info[5] == "":
			return HttpResponse(f"no password  {info}")

		try:
			login = request.session["login"]
			if login == None:
				return HttpResponseRedirect(f"/login/{tableid}")
		except:
			return HttpResponseRedirect(f"/login/{tableid}")

		userInfo = Table().listUsersTable(tablename=tableid)

		if login in str(userInfo):
			pass
		else:
			return render(request, "table_pass.html", {})
		
		return render(request, "table_cal.html", {})
		

	
	def post(self, request, tableid):

		try:
			login = request.session["login"]
		except:
			return HttpResponseRedirect("/login")

		form = Table_password(request.POST)

		if not form.is_valid():
			return render(request, "table_pass.html", {"error": "invalid password"})
		

		password = form.cleaned_data["password"]
		info = Table().getTableInfo(url=tableid)[0]
		
		print(info)
		if info[5] == password:
			status = Table().addUserTable(user=login,url=info[2])
		else:
			return render(request, "table_pass.html", {"error": "invalid password"})

		print("end")
		return HttpResponse(f"no password  {info}")





