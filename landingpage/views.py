from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login

from django.views.generic.list import ListView
from tables.models import Particip

# class LandingPage(View):
# 	def get(self, request):
# 		username = request.session.get("username")
# 		# return render(request, "login.html", headers)
# 		return HttpResponse(username)


class LandingPage(ListView):

	model = Particip
	template_name = "homepage.html"
	http_method_names = ['get']



	def get_queryset(self, **kwargs):
		# context = super().get_context_data(**kwargs)
		user = self.request.session.get("username")
		self.context = Particip.objects.all().filter(user_id__username=user).select_related("user_id")

		# context['now'] = timezone.now()
		return self.context

	def get_context_data(self, **kwargs): 
		ret = dict()
		ret["object_list"] = self.context
		ret["title"] = "Taskmanager"
		ret["username"] = self.request.session.get("username")
		return ret
