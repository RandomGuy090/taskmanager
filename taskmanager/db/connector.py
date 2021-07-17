import taskmanager.db.Db as db
from django.db import connection
from .dbutils import Ddbutils


class UserManagement(Ddbutils):
	def __init__(self):
		self.name = ""
		self.password = ""
	
	def createUser(self, name, password):
		cursor = connection.cursor()
		cursor.execute('''
			insert into taskmanager_user (name, password, profImg, singupDate) values
			("%s", "%s", "%s",%s);
			'''% (name, password, "/static/img/profile.png", "datetime('now')"))
		# try:
		# 	# usr = db.User(name=name, password=password)
		# 	# usr.save()
		# 	return True
		# except:
		# 	return False

	def deleteUser(self, name):
		try:
			cursor = connection.cursor()
			cursor.execute('''SELECT password
				FROM taskmanager_user
			     WHERE
			     name = '%s'
				'''% name)
			return True
		except:
			return False
	
	def getUserInfo(self, name): # dep
		cursor = connection.cursor()
		cursor.execute('''SELECT * 
			FROM taskmanager_user
		     WHERE
		     name = '%s'
			'''% name)

		return cursor.fetchall()


	def getPassword(self, name):
		try:
			cursor = connection.cursor()
			cursor.execute('''SELECT password
				FROM taskmanager_user
			     WHERE
			     name = '%s'
				'''% name)
			res = cursor.fetchall()[0][0]

			return res
		except:
			return False

	def getUsersTables(self, name): 
		cursor = connection.cursor()
		cursor.execute('''SELECT
		     *
		     FROM
		     main_page_info
		     WHERE user = '%s' AND
		     user IS NOT NULL
		     GROUP BY table_url
		     ORDER BY table_id DESC
			'''% name)

		cols = self.getColumn("main_page_info")
		content = cursor.fetchall()

		return self.queryToDict(content=content, column=cols)


class TablesManagement(Ddbutils):

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
		for elem in color:
			print(elem)
			tmp = int(elem, 16) 
			print(tmp)
			tmp -=5
			if tmp < 0: tmp = 0
			print(tmp)
			ret+=str(hex(tmp)[2:])
		return ret
	

	def createTable(self, name, color, password, user): #to opt
		url = self.generate_url()
		cursor = connection.cursor()
		cursor.execute('''
			insert into
			   taskmanager_tables (name, url, color, borderColor, password) 
			values
			   (
			      "%s", "%s", "%s", "%s","%s"
			   ) '''% (name, url, color, self.makeBorderColor(color), password))
		self.addUserTable(user=user, url=url)

		return url

	def addUserTable(self, user, url):
		cursor = connection.cursor()

		cursor.execute('''INSERT 
				into taskmanager_particip (tableId_id, userId_id) 
				values (
				(select id from taskmanager_tables where url = '%s'),
				(select id from taskmanager_user where name = '%s')
				);
				 '''%  (url, user))
		return True



	def getTableInfo(self, url):
		cursor = connection.cursor()
		try:
			cursor.execute('''
				SELECT * 
				FROM taskmanager_tables
				WHERE url = '%s'
				;
			 '''%  url)
			return cursor.fetchall()
		except:
			return False




