import taskmanager.db.Db as db
from django.db import connection
from .JsonConv import ToJson


class UserManagement(ToJson):
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
	
	def getUserInfo(self, name):
		cursor = connection.cursor()
		cursor.execute('''SELECT * 
			FROM taskmanager_user
		     WHERE
		     name = '%s'
			'''% name)

		return cursor.fetchall()


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
		     WHERE taskmanager_user.name = '%s' AND
		     taskmanager_tables.name IS NOT NULL
		     GROUP BY taskmanager_tables.name
		     ORDER BY taskmanager_tables.id DESC
			'''% name)

		return cursor.fetchall()


class TablesManagement(ToJson):
	def getTableInfo(self, link):
		cursor = connection.cursor()

		cursor.execute('''SELECT

			''')
		
		return cursor.fetchall()

	def listUsersTable(self, tablename):
		cursor = connection.cursor()
		
		cursor.execute('''
			SELECT
			 taskmanager_user.name as user,
			 taskmanager_user.profImg as user_prof
			 FROM
			 taskmanager_particip
			 LEFT JOIN taskmanager_user ON taskmanager_particip.userId_id = taskmanager_user.id
			 LEFT JOIN taskmanager_tables ON taskmanager_particip.tableId_id = taskmanager_tables.id
			 WHERE taskmanager_tables.url = "%s" AND
			 taskmanager_tables.name IS NOT NULL
			 GROUP BY user
			 ;
			''' % tablename)
		
		return cursor.fetchall()	
	
	def makeBorderColor(self, color):
		if color.startswith("#"):
			color = color[1:]
		ret = "#"
		print(color)
		print(color)
		print(color)
		for elem in color:
			print(elem)
			tmp = int(elem, 16) 
			print(tmp)
			tmp -=5
			if tmp < 0: tmp = 0
			print(tmp)
			ret+=str(hex(tmp)[2:])
		return ret
	
	def createTable(self, name, color, password):
		
		table = db.Tables(name=name, color=color, 
			borderColor=self.makeBorderColor(color),
			password=password)
		table.save()
		cursor = connection.cursor()
		
		cursor.execute('''SELECT url 
			FROM taskmanager_tables
			WHERE name = '%s' 
			ORDER BY  id DESC '''%  name)
		return cursor.fetchall()[0][0]

	def addUserTable(self, user, table):
		cursor = connection.cursor()
		try:
			cursor.execute('''INSERT into taskmanager_particip (tableId_id, userId_id) 
				values (
			(select id from taskmanager_tables where name = '%s'),
			(select id from taskmanager_user where name = '%s')
			);
			 '''%  (table, user))
			return True
		except:
			return False


