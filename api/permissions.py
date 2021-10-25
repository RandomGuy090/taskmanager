from rest_framework import permissions
from taskmanager.exceptions import (
	ServiceUnavailable,
	Unauthorized,
	NotAdded,
	NoSuchTable,
)
from tables.models import (
	Notes, 
	Tables, 
	Particip
)


from api.tables.utils import (
    get_table_url
)



class CanReadTableContent(permissions.BasePermission):
	"permissions for allowing user read table content"

	# edit_methods = ("PUT", "PATCH")

	def need_password(self) -> bool:
		"does table need password?"

		url = get_table_url(self.URL)
		try:
			password = Tables.objects.filter(url=url).first()
		except:
			# status 404
			raise NoSuchTable
		if not password and password.password == "":
			return False

		return True

	def already_added(self)-> bool:
		"check if user is added to table"
		is_added = Particip.objects.select_related().filter(user_id__username=self.USERNAME, table_id__url=self.table_ID)
		is_added = is_added.exists()
		return is_added


	def has_permission(self, request, view) -> bool:
		"main function"
		self.URL = request.path
		self.table_ID = get_table_url(request.path)
		self.USERNAME = request.user.username


		if request.user.is_authenticated:
			#if user already added to the table
			if self.already_added():
				#if added
				queryset = Particip.objects.select_related().filter(table_id__url=self.table_ID)

				return queryset
			else:
				#not added
				if not self.need_password():
					#table doesn't need password
					queryset = Particip.objects.select_related().filter(table_id__url=self.table_ID)
				else:
					#table needs password and not added
					# status 401
					raise NotAdded

			return True
		else:
			if self.need_password():
				# status 401
				raise Unauthorized

			return True



class CanSendNote(permissions.BasePermission):
	"permissions for allowing user read table content"

	# edit_methods = ("PUT", "PATCH")

	
	def already_added(self)-> bool:
		"check if user is added to table"
		is_added = Particip.objects.select_related().filter(user_id__username=self.USERNAME, table_id__url=self.table_ID)
		is_added = is_added.exists()
		return is_added


	def has_permission(self, request, view) -> bool:
		"main function"
		self.URL = request.path
		self.table_ID = get_table_url(request.path)
		self.USERNAME = request.user.username


		if request.user.is_authenticated:
			return self.already_added()

		else:
			raise Unauthorized

			#return True