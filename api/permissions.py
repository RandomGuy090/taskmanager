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

	edit_methods = ("PUT", "PATCH")
	
	# def get_url(self):
	# 	"get table id from url"

	# 	url = self.URL
	# 	if url.endswith("/"):
	# 		url=url[:-1]
	# 	spl = url.split("/")
	# 	# url = spl[spl.index(spl[-1])-1]
	# 	url = spl[spl.index(spl[3])]
		
	# 	#makeshift
	# 	if len(url) == 16:
	# 		self.table_ID = url
	# 		return url
	# 	else: 
	# 		# url = spl[spl.index(spl[-1])]
	# 		url = spl[spl.index(spl[3])]
	# 		self.table_ID = url
	# 		return url


	def need_password(self):
		"does table need password?"

		# url = get_table_url(request.path)
		url = get_table_url(self.URL)

		try:
			password = Tables.objects.filter(url=url).first()
		except:
			raise NoSuchTable
		
		if not password and password.password == "":
			return False
		return True

	def already_added(self):
		"check if user is added to table"
		is_added = Particip.objects.select_related().filter(user_id__username=self.USERNAME, table_id__url=self.table_ID)
		is_added = is_added.exists()
		return is_added


	def has_permission(self, request, view):
		#fist
		"main function"
		self.URL = request.path
		self.table_ID = get_table_url(request.path)
		self.USERNAME = request.session.get("username")

		if request.user.is_authenticated:
			#id logged
			if self.already_added():
				#if added
				queryset = Particip.objects.select_related().filter(table_id__url=self.table_ID)
				return queryset
			else:
				#not added
				if not self.need_password():
					#table doesn;t need password
					queryset = Particip.objects.select_related().filter(table_id__url=self.table_ID)
				else:
					#table needs password and not added
					raise NotAdded

			return True
		else:
			if self.need_password():
				raise Unauthorized
			return True



# class CanReadTable(permissions.BasePermission):

# 	def has_permission(self, requset, view):

