from rest_framework import viewsets
from api.permissions import CanReadTableContent
from tables.models import Notes
from api.serializer import 	NotesSerializer

from .utils import 	get_table_url


class Notes_view(viewsets.ModelViewSet):
	queryset = Notes.objects.all()
	serializer_class = NotesSerializer
	lookup_field = "id"
	permission_classes = [CanReadTableContent]

	def get_queryset(self):
		url = get_table_url(self.request.path)

		year = self.request.query_params.get("year") 
		month = self.request.query_params.get("month")
		day = self.request.query_params.get("day")

		
		if year and month and day:
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__year=int(year),
						todo_date_start__month=int(month),
						todo_date_start__day=int(day))
		elif year and month :
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__year=int(year),
						todo_date_start__month=int(month))
		elif year :
			queryset = Notes.objects.select_related().filter(table_id__url=url,
						todo_date_start__year=int(year))
		else:
			queryset = Notes.objects.select_related().filter(table_id__url=url)
		
		return queryset

