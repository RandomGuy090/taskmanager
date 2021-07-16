from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from taskmanager.db.connector import UserManagement as User
from taskmanager.db.connector import TablesManagement as Table



class Tables(View):
	def get(self, request, tableid):
		print(tableid)

		userInfo = Table().listUsersTable(tablename=tableid)
		return HttpResponse(userInfo)



