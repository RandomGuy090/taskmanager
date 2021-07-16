import json, sys


def getUsersTables(name):
	cursor = connection.cursor()
	cursor.execute('''
		SELECT * from main_page_info
		 WHERE user = "%s" AND
		 table_name IS NOT NULL
		 GROUP BY table_name
		 ORDER BY table_id DESC
		'''% name)
	return cursor.fetchall()



def getCols(name):
	cursor = connection.cursor()
	cursor.execute('''
		SELECT name FROM pragma_table_info('%s') JOIN (SELECT COUNT(*) FROM %s);
		''' % (name, name))
	return cursor.fetchall()

users =[('admin', '/static/img/profile.png', 19, 'asdfsadf', 'omqaotxmgvhadjov', '#000000', '#000000'), ('admin', '/static/img/profile.png', 18, 'asdf', 'puopghztinqtkczv', '#808080', '#303030'), ('admin', '/static/img/profile.png', 17, 'testing2', 'twhuphmasplpieup', '#ff00e1', '#aa0090'), ('admin', '/static/img/profile.png', 13, 'asdfsddssdfsdfsdfsdf', 'hpkinqfpgfhqeubo', '#00ff1e', '#00aa09'), ('admin', '/static/img/profile.png', 11, 'testing 1', 'yfoshcjzgetotjzf', '#d1dfff', '#808aaa'), ('admin', '/static/img/profile.png', 10, 'new_url_methodasdf', 'xkmfymtzhcmudrqq', '#0059ff', '#0004aa'), ('admin', '/static/img/profile.png', 7, 'testing asdlfasdf', 'arsfximkkhwmvwkw', '#ff0000', '#aa0000'), ('admin', '/static/img/profile.png', 6, 'sadf', 'bnfxgwhyihstzyfg', '#000000', '#000000'), ('admin', '/static/img/profile.png', 5, 'aasdfsdafsadf', 'sitmlfwtyavgwgpi', '#00ffd5', '#00aa80'), ('admin', '/static/img/profile.png', 4, 'admin', 'qcusvmqrtwvcfqub', '#ff00f7', '#aa00a2'), ('admin', '/static/img/profile.png', 3, 'dfgshdfdfsg', 'znmhckgfqjmorgtq', '#fbff00', '#a6aa00'), ('admin', '/static/img/profile.png', 2, 'asdfasdf', 'wdznbwbkloyrsura', '#00ff7b', '#00aa26'), ('admin', '/static/img/profile.png', 1, '1st', 'aghblupljuycqmwg', '#e33535', '#900000')]

table =[('user',), ('prof_pic',), ('table_id',), ('table_name',), ('table_url',), ('table_color',), ('table_b_color',)]


# users = getUsersTables(name="admin")
# print(users)
# table = getCols(name="main_page_info")
# print(table)


# cols = list()
# for elem in table:
# 	cols.append(elem[0])

# # print(cols)

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
	# ret = json.dumps(ret)

print(prepareJson(users, table, "table_url"))


# ret = dict()

# for user in users:
# 	print(user)
# 	tmp = {}
# 	for pos, val in enumerate(user):
# 		print(pos, val)
# 		tmp[table[pos][0]] = val
# 	ret[tmp["user"]]= tmp

# ret = json.dumps(ret)
# print(ret)


