from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
	status_code = 503
	default_detail = 'Service temporarily unavailable, try again later.'
	default_code = 'service_unavailable'


class Unauthorized(APIException):
	status_code = 401
	default_detail = 'Authorization required'
	default_code = 'Unauthorized'


class NoSuchTable(APIException):
	status_code = 404
	default_detail = 'No such table'
	default_code = 'Not found'


class NotAdded(APIException):
	status_code = 401
	default_detail = 'User not added to the table'
	default_code = 'Unauthorized'
	

class NullFields(APIException):
	status_code = 404
	default_detail = "Null fields"
	default_code = "invalid"

	def __init__(self, detail):
		if detail is not None:
			self.detail = f" Null fields: {detail}"
