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


    def get_queryset(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = Particip.objects.all().filter(user_id__username="admin").select_related("user_id")
        for elem in context:
        	print(elem.user_id.username, elem.table_id.name)

        # context['now'] = timezone.now()
        return context
