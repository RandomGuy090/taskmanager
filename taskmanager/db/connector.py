# import taskmanager.db.Db as db
from django.db import connection
from .dbutils import Ddbutils
from django.db.utils import OperationalError

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
		     user IS NOT NULL AND
		     table_url IS NOT NULL
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

	def listUsersTable(self, tablename="", url=""):
		cursor = connection.cursor()
		taken = False;
		if tablename != "" and not taken:
			cursor.execute('''
				SELECT 
				* 
				FROM
				list_users_table
				WHERE table_name = "%s" AND
				table_name IS NOT NULL
				GROUP BY user_name
				 ;
				''' % tablename)
			taken = True

		elif url != "" and not taken:
			cursor.execute('''
				SELECT 
				* 
				FROM
				list_users_table
				WHERE table_url = "%s" AND
				table_name IS NOT NULL
				GROUP BY user_name
				 ;
				''' % url)
			taken = True

			
		cols = self.getColumn("list_users_table")
		content = cursor.fetchall()

		return self.queryToDict(content=content, column=cols)

		
	
	def makeBorderColor(self, color):
		if color.startswith("#"):
			color = color[1:]
		ret = "#"
		for elem in color:
			
			tmp = int(elem, 16) 
			tmp -=5
			if tmp < 0: tmp = 0
			ret+=str(hex(tmp)[2:])
		return ret
	

	def createTable(self, name, color, password, user): #to opt
		url = self.generate_url()
		cursor = connection.cursor()
		# passwordNeeded = True if password != "" else False
		passwordNeeded = True

		cursor.execute(''' 
			INSERT INTO
			   taskmanager_tables (name, url, color, borderColor, password, passwordNeeded) 
			values
			   (
			      "%s", "%s", "%s", "%s","%s", "%s"
			   );

			'''% (name, url, color, self.makeBorderColor(color), password, passwordNeeded))
		
		self.addUserTable(user=user, url=url)

		return url

	def leaveTable(self, url=""):
		cursor = connection.cursor()
		url = cursor.execute(''' 
			DELETE 
			FROM 
			taskmanager_particip
			WHERE 
			id =
			(SELECT 
			id
			FROM 
			taskmanager_tables
			WHERE
			url = '%s'
			)'''% url)
		res = cursor.execute

	def deleteTable(self, url=""):
		cursor = connection.cursor()
		url = cursor.execute(''' 
			DELETE 
			FROM 
			taskmanager_particip
			WHERE 
			id =
			(SELECT 
			id
			FROM 
			taskmanager_tables
			WHERE
			url = '%s'
			)'''% url)
		res = cursor.execute


	def addUserTable(self, user, url):
		cursor = connection.cursor()
		print("addUserTable")
		cursor.execute(''' 
			SELECT 
			user_name 
			FROM
			list_users_table 
			WHERE  
			table_url = "%s"
			AND
			user_name = "%s" 
			GROUP BY
			user_name
			;

			 '''%  (url, user))
		res = cursor.fetchall();
		if res != []:
			print("user already added")
			return False

		print(res)
		print(res)
		print(res)
		print(res)
		print("add user")
		cursor.execute('''INSERT 
			into taskmanager_taskcolor (tableId_id, userId_id, color) 
			values (
			(select id from taskmanager_tables where url = '%s'),
			(select id from taskmanager_user where name = '%s'),
			"%s"
			);
			 '''%  (url, user, self.genColor() ))


		cursor.execute('''INSERT 
				into taskmanager_particip (tableId_id, userId_id, color_id, joinedDate) 
				values (
				(select id from taskmanager_tables where url = '%s'),
				(select id from taskmanager_user where name = '%s'),
				(select id from taskmanager_taskcolor where userId_id = (
				select id from taskmanager_user where name = '%s')),
				datetime("now")
				);
				 '''%  (url, user, user ))
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
			cols = self.getColumn("taskmanager_tables")
			content = cursor.fetchall()

			return self.queryToDict(content=content, column=cols)
		except:
			return False


	def getTableColor(self, url):
		cursor = connection.cursor()
		try:
			cursor.execute('''
				SELECT * 
				from 
				get_table_color 
				where 
				table_url = "%s"
				;
			 '''%  url)
			cols = self.getColumn("get_table_color")
			content = cursor.fetchall()

			res = self.queryToDict(content=content, column=cols)
			print(res)
			return res
		except:
			return False
	



class TasksManagement(Ddbutils):

	def getMonth(self, month, year, url):
		cursor = connection.cursor()

		if len(str(month)) == 1:
			month = f"0{month}"
		
		dateFrom = f"{year}-{month}-01"
		dateTo = f"{year}-{month}-31"
		cursor.execute('''
			select 
			* 
			from 
			get_tasks
			WHERE table_name IS NOT NULL 
			AND added_date IS NOT NULL 
			AND strftime('%%Y-%%m-%%d', to_do_date_start) >= date("%s-%s-01")
			AND strftime('%%Y-%%m-%%d', to_do_date_end) <= date("%s-%s-31")
			AND table_url = "%s"
			GROUP BY user_id, table_url, note_id
			ORDER BY to_do_date_start ASC
			;
			 '''%  (year, month, year, month, url))
		try:
			cols = self.getColumn("get_tasks")
			content = cursor.fetchall()
			print("content")
			print("content")
			print("content")
			print(content)
			response = self.queryToDict(content=content, column=cols)
			
			if len(response) == 0:
				response= {
				"success": False,
				"error": "no tasks"
				}

			return response
		except:
			response= {
				"success": False,
				"error": "server failure"
				}
			return response

	def getYear(self, year, url):
		cursor = connection.cursor()
		if len(year) != 4:
			response= {
				"success": False,
				"error": "year must be 4 digit"
				}

			return response
		cursor.execute('''
			select 
			* 
			from 
			get_tasks
			WHERE table_name IS NOT NULL 
			AND added_date IS NOT NULL 
			AND strftime('%%Y-%%m-%%d', to_do_date_start) >= date("%s-01-01")
			AND strftime('%%Y-%%m-%%d', to_do_date_end) <= date("%s-12-31")
			AND table_url = "%s"
			GROUP BY user_id, table_url, note_id
			ORDER BY to_do_date_start ASC
			;
			
			 '''%  (year, year, url))
		try:
			cols = self.getColumn("get_tasks")
			content = cursor.fetchall()
			response = self.queryToDict(content=content, column=cols)
			
			if len(response) == 0:
				response= {
				"success": False,
				"error": "no tasks"
				}

			return response
		except:
			response= {
				"success": False,
				"error": "server failure"
				}
			return response


	def getDay(self, year, month, day, url):
		
		cursor = connection.cursor()
		
		if len(year) != 4:
			response= {
				"success": False,
				"error": "year must be 4 digit"
				}

			return response
		if len(str(month)) == 1:
			month = f"0{month}"

		if len(str(day)) == 1:
			month = f"0{day}"

		cursor.execute('''
			select 
			* 
			from 
			get_tasks
			WHERE table_name IS NOT NULL 
			AND added_date IS NOT NULL 
			AND strftime('%%Y-%%m-%%d', to_do_date_start) >= date("%s-%s-%s")
			AND table_url = "%s"
			GROUP BY user_id, table_url, note_id
			ORDER BY to_do_date_start ASC
			;
			
			 '''%  (year,month, day, url))
		try:
			cols = self.getColumn("get_tasks")
			content = cursor.fetchall()
			response = self.queryToDict(content=content, column=cols)
			print(response)
			
			if len(response) == 0:
				response= {
				"success": False,
				"error": "no tasks"
				}

			return response
		except:
			response= {
				"success": False,
				"error": "server failure"
				}

			return response

	def createTask(self, date_start, date_end, user, content, url):
		cursor = connection.cursor()
		cursor.execute('''
		insert into taskmanager_notes 
		(tableNote, addedDate, todoDate_start, todoDate_end, tableId_id, userId_id) 
		
		values("%s", datetime("now"), "%s", "%s", 
		(select id from taskmanager_tables where url = "%s"),
		(select id from taskmanager_user where name = "%s")
		)
		;
		'''%  (content ,date_start, date_end ,url, user))
		try:
			return True
		except :
			return False		



class LoadStartUp(object):
	def __init__(self, file):

		cont = ""
		with open(file, "r") as f:
			cont = f.read()
		cont = cont.split(";")
		cursor = connection.cursor()
		for elem in cont:
			try:
				cursor.execute(elem)
			except OperationalError:
				print("------> cannot create")
				print(elem.split("as")[0])





