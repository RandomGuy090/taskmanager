from django.db import models
#to get from taskmanager.Db import ToDoList, Item
import random
def genUrl(lenght=16):
	rstr = ""
	for _ in range(lenght):
	    integ = random.randint(97, 97 + 26 - 1)
	    rstr += (chr(integ))
	return rstr

class User(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	singupDate = models.DateTimeField(auto_now_add=True, blank=True)

class Tables(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=16, default=genUrl)
	color = models.CharField(max_length=7, default="#B5E61")
	borderColor = models.CharField(max_length=7, default="#8CAE22")

class Particip(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)

#FF0000