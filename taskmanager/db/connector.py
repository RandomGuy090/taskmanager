# import taskmanager.db._db as db
from django.db import connection
from .dbutils import DButils
from django.db.utils import OperationalError, IntegrityError

class User_management(DButils):
	def __init__(self):
		self.name = ""
		self.password = ""
	
	def create_user(self, name, password):
		cursor = connection.cursor()
		try:
			cursor.execute('''
				insert into taskmanager_user (name, password, prof_img, singup_date) values
				("%s", "%s", "%s",%s);
				'''% (name, password, "/img/profile.png", "datetime('now')"))
		except IntegrityError:
			return "user with this name already exist"


	def delete_user(self, name):
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
	
	def get_user_info(self, name): # dep
		cursor = connection.cursor()
		cursor.execute('''SELECT * 
			FROM taskmanager_user
		     WHERE
		     name = '%s'
			'''% name)

		return cursor.fetchall()


	def get_password(self, name):
		try:
			cursor = connection.cursor()
			cursor.execute('''SELECT password
				FROM taskmanager_user
			     WHERE
			     name = '%s'
				'''% name)
			res = cursor.fetchall()[0][0]
			print(res)
			print(res)
			print(res)
			print(res)

			return res
		except:
			return False

	def get_users_tables(self, name): 
		cursor = connection.cursor()
		cursor.execute('''SELECT
		     *
		     FROM
		     main_page_info
		     WHERE user = '%s' AND
		     user IS NOT NULL AND
		     table_url IS NOT NULL
		     GROUP BY table_url
		     ORDER BY table_id 
			'''% name)

		cols = self.get_column("main_page_info")
		content = cursor.fetchall()

		return self.query_to_dict(content=content, column=cols)


class Tables_management(DButils):

	def get_table_info(self, link):
		cursor = connection.cursor()

		cursor.execute('''SELECT
			''')
		
		return cursor.fetchall()

	def list_users_table(self, tablename="", url=""):
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

			
		cols = self.get_column("list_users_table")
		content = cursor.fetchall()

		tmp = self.query_to_dict(content=content, column=cols)

		return self.users_of_table(tmp)

		
	
	def make_border_color(self, color):
		if color.startswith("#"):
			color = color[1:]
		ret = "#"
		for elem in color:
			
			tmp = int(elem, 16) 
			tmp -=5
			if tmp < 0: tmp = 0
			ret+=str(hex(tmp)[2:])
		return ret
	

	def create_table(self, name, color, password, user): #to opt
		url = self.generate_url()
		cursor = connection.cursor()
		# password_needed = True if password != "" else False
		password_needed = True

		cursor.execute(''' 
			INSERT INTO
			   taskmanager_tables (name, url, color, border_color, password, password_needed) 
			values
			   (
			      "%s", "%s", "%s", "%s","%s", "%s"
			   );

			'''% (name, url, color, self.make_border_color(color), password, password_needed))
		
		self.add_user_table(user=user, url=url)

		return url

	def leave_table(self, url=""):
		cursor = connection.cursor()
		url = cursor.execute(''' 
			s 
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

	def delete_table(self, url=""):
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


	def add_user_table(self, user, url):
		cursor = connection.cursor()
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
			return False

		cursor.execute('''INSERT 
			into taskmanager_task_color (table_id_id, user_id_id, color) 
			values (
			(select id from taskmanager_tables where url = '%s'),
			(select id from taskmanager_user where name = '%s'),
			"%s"
			);
			 '''%  (url, user, self.gen_color() ))


		cursor.execute('''INSERT 
				into taskmanager_particip (table_id_id, user_id_id, color_id, joined_date) 
				values (
				(select id from taskmanager_tables where url = '%s'),
				(select id from taskmanager_user where name = '%s'),
				(select id from taskmanager_task_color where user_id_id = (
				select id from taskmanager_user where name = '%s')),
				datetime("now")
				);
				 '''%  (url, user, user ))
		return True



	def get_table_info(self, url):
		cursor = connection.cursor()
		try:
			cursor.execute('''
				SELECT * 
				FROM taskmanager_tables
				WHERE url = '%s'
				;
			 '''%  url)
			cols = self.get_column("taskmanager_tables")
			content = cursor.fetchall()

			return self.query_to_dict(content=content, column=cols)
		except:
			return False


	def get_table_color(self, url):
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
			cols = self.get_column("get_table_color")
			content = cursor.fetchall()

			res = self.query_to_dict(content=content, column=cols)
			return res
		except:
			return False
	



class Tasks_management(DButils):

	def get_month(self, month, year, url):
		cursor = connection.cursor()

		if len(str(month)) == 1:
			month = f"0{month}"
		
		dateFROM = f"{year}-{month}-01"
		date_to = f"{year}-{month}-31"
		cursor.execute('''
			SELECT 
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
			cols = self.get_column("get_tasks")
			content = cursor.fetchall()
			response = self.query_to_dict(content=content, column=cols)
			
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
			SELECT 
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
			cols = self.get_column("get_tasks")
			content = cursor.fetchall()
			response = self.query_to_dict(content=content, column=cols)
			
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


	def get_day(self, year, month, day, url):
		
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
			SELECT 
			* 
			from 
			get_tasks
			WHERE table_name IS NOT NULL 
			AND added_date IS NOT NULL 
			AND strftime('%%Y-%%m-%%d', to_do_date_end) >= date("%s-%s-%s")
			AND strftime('%%Y-%%m-%%d', to_do_date_start) <=  date("%s-%s-%s")
			AND table_url = "%s"
			GROUP BY user_id, table_url, note_id
			ORDER BY to_do_date_start ASC
			;

			
			 '''%  (year,month, day, year,month, day, url))

		try:
			content = cursor.fetchall()
			cols = self.get_column("get_tasks")
			response = self.query_to_dict(content=content, column=cols)
			
			
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

	def create_task(self, date_start, date_end, user, content, url):
		cursor = connection.cursor()
		cursor.execute('''
		INSERT into taskmanager_notes 
		(table_note, added_date, todo_date_start, todo_date_end, table_id_id, user_id_id) 
		
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



class Load_start_up(object):
	def __init__(self, file):

		cont = ""
		cursor = connection.cursor()
		try:
			cursor.execute("SELECT *  from taskmanager_user").fetchall()
		except OperationalError:
			return 
		with open(file, "r") as f:
			cont = f.read()
		cont = cont.split(";")
		for elem in cont:
			try:
				cursor.execute(elem)
			except OperationalError:
				pass





