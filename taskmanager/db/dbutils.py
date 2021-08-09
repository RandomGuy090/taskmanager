from django.db import connection
import random


class DButils(object):

	def get_column(self, name):
		cursor = connection.cursor()
		cursor.execute('''
			SELECT name FROM pragma_table_info('%s') 
			JOIN (SELECT COUNT(*) FROM %s);

			'''% (name, name))

		return cursor.fetchall()

	def query_to_dict(self, content, column, index=""):
		'''
		content e.g. =[('foo', 'bar')]
		table e.g. = [('foo',), ('bar',)]
		index e.g. = "table_id"
		'''
		ret = list()
		if index != "":
			ret = dict()

		for user in content:
			tmp = {}
			for pos, val in enumerate(user):
				tmp[column[pos][0]] = val
			
			if index != "":
				ret[tmp[index]]= tmp
			else:
				ret.append(tmp)


		return ret

	def generate_url(self, lenght=16):
		rstr = ""
		for _ in range(lenght):
		    integ = random.randint(97, 97 + 26 - 1)
		    rstr += (chr(integ))
		return rstr

	def get_table_cols(self, table):
		cursor = connection.cursor()
		cursor.execute('''
			SELECT name FROM pragma_table_info('%s') 
			JOIN (SELECT COUNT(*) 
			FROM %s);
			'''% (table, table))

		cols = cursor.fetchall()
		res = []
		for elem in cols:
			res.append(elem[0])
		return res

	def cols_to_data(self, table, users, field):

		ret = dict()
		for user in users:
			tmp = {}
			for pos, val in enumerate(user):
				tmp[table[pos]] = val
			ret[tmp[field]]= tmp
		return ret

	def user_info_sort_id(self, name=None):
		cursor = connection.cursor()
		if name == None:
			cursor.execute('''SELECT * 
				FROM taskmanager_user
				''')
			users = cursor.fetchall()

		elif name:
			cursor.execute('''SELECT * 
				FROM taskmanager_user
				where 
				name = '%s'
				'''% name)
			users = cursor.fetchall()

		return self.cols_to_data(self.get_table_cols("taskmanager_user"), users, "id")

	def user_info_sort_name(self, name=None):
		cursor = connection.cursor()
		if name == None:
			cursor.execute('''SELECT * 
				FROM taskmanager_user
				''')
			users = cursor.fetchall()

		elif name:
			cursor.execute('''SELECT * 
				FROM taskmanager_user
				where 
				name = '%s'
				'''% name)
			users = cursor.fetchall()

		return self.cols_to_data(self.get_table_cols("taskmanager_user"), users, "id")

	def gen_color(self):
		ret = "#"
		for i in range(3):
			r = random.randrange(0, 255)
			r = hex(r)[2:]
			ret += r
		return ret


