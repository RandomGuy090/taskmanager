import taskmanager.db.Db as db
from django.db import connection

class UserManagement(object):
	def __init__(self):
		self.name = ""
		self.password = ""

	def createUser(self, name, password):
		try:
			usr = db.User(name=name, password=password)
			usr.save()
			return True
		except:
			return False

	def deleteUser(self, name):
		try:
			usr = db.User.objects.get(name=name)
			usr.delete()
			usr.save()
			return True
		except:
			return False
	
	def getPassword(self, name):
		try:
			usr = db.User.objects.get(name=name)
			return usr.password
		except:
			return False

	def getUsersTables(self, name):
		cursor = connection.cursor()
		cursor.execute('''SELECT
		     taskmanager_user.name,
		     taskmanager_tables.name,
		     taskmanager_tables.url,
		     taskmanager_tables.color,
		     taskmanager_tables.borderColor
		     FROM
		     taskmanager_particip
		     LEFT JOIN taskmanager_user ON taskmanager_particip.userId_id = taskmanager_user.id
		     LEFT JOIN taskmanager_tables ON taskmanager_particip.tableId_id = taskmanager_tables.id
		     WHERE
		     taskmanager_user.name = '%s'
			'''% name)

		return cursor.fetchall()



