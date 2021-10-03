from rest_framework import viewsets
from api.permissions import CanReadTableContent
from tables.models import Notes
from api.serializer import 	NotesSerializer
from rest_framework.response import Response
from .utils import 	get_table_url

from taskmanager.exceptions import NullFields

class Notes_view(viewsets.ModelViewSet):
	"list all notes in table"

	serializer_class = NotesSerializer
	lookup_field = "id"
	permission_classes = [CanReadTableContent]

	def get_queryset(self):
		#get url of table
		url = get_table_url(self.request.path)
		#get query params
		year = self.request.query_params.get("year") 
		month = self.request.query_params.get("month")
		day = self.request.query_params.get("day")

		#get one day
		if year and month and day:
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__year=int(year),
						todo_date_start__month=int(month),
						todo_date_start__day=int(day))
		#get one month
		elif year and month :
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__year=int(year),
						todo_date_start__month=int(month))
		#get one year
		elif year :
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__year=int(year))
		
		#get all notes from table
		else:
			queryset = Notes.objects.select_related().filter(table_id__url=url)
		
		return queryset
	def create(self, request, *args, **kwargs):
		"create new task via post"

		null_fields = []
		for elem in request.data:
			if request.data.get(elem) == "":
				null_fields.append(elem)

		if len(null_fields) != 0:
			raise NullFields(detail=null_fields)
		
		serializer = self.serializer_class(detail=request.data)

		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
		else:
			return Response('Invalid request')


