
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth import get_user_model
from django.db.models import Count

from rest_framework import (
	routers, 
	serializers, 
	viewsets
)
from rest_framework.permissions import IsAuthenticated
from api.permissions import CanReadTableContent
User = get_user_model()

from taskmanager.exceptions import (
	ServiceUnavailable,
	Unauthorized,
	NotAdded,
)

from tables.models import (
	Notes, 
	Tables, 
	Particip
)
from .utils import get_lookup
from api.serializer import (
	TablesSerializerList, 
	TablesSerializerDetail,
	TablesCreateSerializer
)

from django.db.models.query import QuerySet

class Table_view(viewsets.ModelViewSet):
	"list all tables"

	lookup_field = "url"
	http_method_names = ['get']


	def get_serializer_class(self):
		if self.action == "list":
			return TablesSerializerList
		elif self.action == "revive":
			return TablesCreateSerializer

		return TablesSerializerDetail


	def get_queryset(self) :
		try:
			url = get_lookup(self.request.path)
			if len(url) == 16:
				qr = Tables.objects.filter(url=url)
				return qr
			else:
				raise 
		except:
			user = self.request.session.get("username")
			pr = Particip.objects.raw("""SELECT * FROM tables_particip
										JOIN 	tables_tables ON table_id_id
										GROUP BY table_id_id""")
			# pr = Particip.objects.filter(user_id__username=user)

			# query = Particip.objects.all().query
			# query.group_by = ['id']
			# pr = QuerySet(query=query, model=Particip)

			
			# print(pr)



			return pr


