from django.db import connection
import random


class Ddbutils(object):

	def prepareDict(content, column, index):
		'''
		content e.g. =[('foo', 'bar')]
		table e.g. = [('foo',), ('bar',)]
		index e.g. = "table_id"
		'''
		ret = dict()
		for user in users:
			tmp = {}
			for pos, val in enumerate(user):
				tmp[table[pos][0]] = val
			ret[tmp["table_url"]]= tmp

		return ret
		
	def generate_url(self, lenght=16):
		rstr = ""
		for _ in range(lenght):
		    integ = random.randint(97, 97 + 26 - 1)
		    rstr += (chr(integ))
		return rstr

	def getTableCols(self, table):
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

	def colsToData(self, table, users, field):

		ret = dict()
		for user in users:
			tmp = {}
			for pos, val in enumerate(user):
				tmp[table[pos]] = val
			ret[tmp[field]]= tmp
		return ret

	def userInfoSortID(self, name=None):
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

		return self.colsToData(self.getTableCols("taskmanager_user"), users, "id")

	def userInfoSortName(self, name=None):
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

		return self.colsToData(self.getTableCols("taskmanager_user"), users, "id")


