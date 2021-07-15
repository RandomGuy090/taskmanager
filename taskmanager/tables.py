from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render


class Tables(View):
	def get(self, request, tableid):
		print(tableid)
		return HttpResponse(tableid)



