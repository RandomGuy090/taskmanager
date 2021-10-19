from rest_framework import viewsets
from api.permissions import CanReadTableContent
from tables.models import Notes
from api.serializer import 	NotesSerializer
from rest_framework.response import Response
from .utils import 	get_table_url

import datetime
from calendar import monthrange

from taskmanager.exceptions import (
	NullFields,
	CantDeleteNote,
	NoSuchTable,
)

class Notes_view(viewsets.ModelViewSet):
	"list all notes in table"

	serializer_class = NotesSerializer
	lookup_field = "id"
	permission_classes = [CanReadTableContent]
	http_method_names = ['post', "get", "delete"]


	def get_queryset(self):
		#get url of table
		url = get_table_url(self.request.path)
		#get query params
		year = self.request.query_params.get("year") 
		month = self.request.query_params.get("month")
		day = self.request.query_params.get("day")

		#get one day
		if year and month and day:
			print(day)
			date = datetime.date(int(year), int(month), int(day)+1)
			date2 = datetime.date(int(year), int(month), int(day))
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__lte=date,
						todo_date_end__gte=date2)
			

			# queryset = Notes.objects.select_related().filter(table_id__url=url,
			# 			todo_date_start__year__lte=int(year),
			# 			todo_date_end__year__gte=int(year),

			# 			todo_date_start__month__lte=int(month),
			# 			todo_date_end__month__gte=int(month),
						
			# 			todo_date_start__day__lte=int(day),
			# 			todo_date_end__day__gte=int(day))
		#get one month
		elif year and month :
			date = datetime.date(int(year), int(month), 1)
			date2 = datetime.date(int(year), int(month), monthrange(int(year), int(month))[1])
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__lte=date2,
						todo_date_end__gte=date)

			# queryset = Notes.objects.select_related().filter(table_id__url=url,
			# 			todo_date_start__year__lte=int(year),
			# 			todo_date_end__year__gte=int(year),
			# 			todo_date_start__month__lte=int(month),
			# 			todo_date_end__month__gte=int(month))
		#get one year
		elif year :
			date = datetime.date(int(year), 1, 1)
			date2 = datetime.date(int(year), 12, monthrange(int(year), int(month))[1])
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__lte=date2,
						todo_date_end__gte=date)

			# queryset = Notes.objects.select_related().filter(table_id__url=url,
			# 			todo_date_start__year__lte=int(year),
			# 			todo_date_end__year__gte=int(year))

		
		#get all notes from table
		else:
			queryset = Notes.objects.select_related().filter(table_id__url=url)
		
		
		
		print(queryset)
		return queryset

	def create(self, request, *args, **kwargs):
		"create new task via post"

		null_fields = []
		for elem in request.data:
			if request.data.get(elem) == "":
				null_fields.append(elem)
				
		null_fields.remove("added_date")

		if len(null_fields) != 0:
			raise NullFields(detail=null_fields)

		if not request.POST._mutable:
			request.POST._mutable = True

		request.data["user_id"] = self.request.session.get("username")

		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
		else:
			return Response('Invalid request')

	def destroy(self, request, *args, **kwargs):
		post_id = kwargs.get("id")
		user = self.request.session.get("username")
		
		if post_id:
			qr = Notes.objects.filter(id=post_id, user_id__username=user)
			if qr.exists():
				self.perform_destroy(qr)
				raise NoSuchTable()

			else:
				raise CantDeleteNote(detail="You are not note's author so you can'r delete it")





