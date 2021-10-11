from rest_framework.exceptions import APIException

class LoginOK(APIException):
	status_code = 200
	default_detail = 'Logged ok'
	default_code = 'OK'

class LogoutOK(APIException):
	status_code = 200
	default_detail = 'Logout ok'
	default_code = 'OK'

class RegisterOK(APIException):
	status_code = 200
	default_detail = 'Register ok'
	default_code = 'OK'


class Unauthorized(APIException):
	status_code = 401
	default_detail = 'Authorization required'
	default_code = 'Unauthorized'

class NotLogged(APIException):
	status_code = 401
	default_detail = 'Not logged'
	default_code = 'Unauthorized'

class BadLoginOrPassword(APIException):
	status_code = 401
	default_detail = 'Bad login or password'
	default_code = 'Unauthorized'

class NotAdded(APIException):
	status_code = 401
	default_detail = 'User not added to the table'
	default_code = 'Unauthorized'
	
class PassowordNeeded(APIException):
	status_code = 401
	default_detail = "No password or password incorrect"
	default_code = "Unauthorized"

class LeftTable(APIException):
	status_code = 401
	default_detail = 'Left table'
	default_code = 'Unauthorized'

class NoSuchTable(APIException):
	status_code = 404
	default_detail = 'No such table'
	default_code = 'Not found'

class NullFields(APIException):
	status_code = 404
	default_detail = "Null fields"
	default_code = "invalid"

	def __init__(self, detail=None):
		if detail is not None:
			self.detail = f" Null fields: {detail}"

class CantDeleteNote(APIException):
	status_code = 404
	default_detail = "Can't delete note"
	default_code = "invalid"
	
	def __init__(self, detail=None):
		if detail is not None:
			self.detail = detail
			

class ServerError(APIException):
	status_code = 500
	default_detail = "serializer error"
	default_code = "server error"
	
class ServiceUnavailable(APIException):
	status_code = 503
	default_detail = 'Service temporarily unavailable, try again later.'
	default_code = 'service_unavailable'