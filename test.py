import json

users = [(7, 'janusz', 'paweł', "datetime.datetime(2021, 7, 14, 0, 5, 20, 785162)", '/static/img/profile.png'), (10, 'admin', 'password', "datetime.datetime(2021, 7, 14, 1, 12, 21, 615629)", '/static/img/profile.png'), (11, 'adam', 'password', "datetime.datetime(2021, 7, 14, 19, 21, 30, 57149)", '/static/img/profile.png')]
table = [('id',), ('name',), ('password',), ('singupDate',), ('profImg',)]
cols = list()
for elem in table:
	cols.append(elem[0])

# print(cols)
ret = dict()

for user in users:
	print(user)
	tmp = {}
	for pos, val in enumerate(user):
		print(pos, val)
		tmp[table[pos][0]] = val
	ret[tmp["id"]]= tmp

ret = json.dumps(ret)
print(ret)