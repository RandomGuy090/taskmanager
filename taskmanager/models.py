from django.db import models
#to get from taskmanager.Db import ToDoList, Item
import random
from datetime import datetime
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
	profImg = models.CharField(max_length=100, default="/img/profile.png")


class Tables(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=16, default=genUrl)
	color = models.CharField(max_length=7, default="#B5E61")
	borderColor = models.CharField(max_length=7)
	password = models.CharField(max_length=200, default="")
	passwordNeeded = models.BooleanField(default=False)

class TaskColor(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)
	color = models.CharField(max_length=7, default="")

class Particip(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE, )
	tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)
	color = models.ForeignKey(TaskColor, on_delete=models.CASCADE)
	joinedDate = models.DateTimeField(auto_now_add=True, blank=True)

	
	# class Meta:
	# 	unique_together= (('userId', 'tableId'),)



class Notes(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)
	tableNote = models.CharField(max_length=500, default="")
	addedDate = models.DateTimeField(auto_now_add=True, blank=True)
	todoDate_start = models.DateTimeField(blank=True)
	# todoDate_end = models.DateTimeField(blank=True)


	

# db.Notes(
# userId=db.User.objects.get(name="admin"),
# tableId=db.Tables.objects.get(name="testing1"),
# tableNote="testing note2",
# todoDate=datetime.strptime("","").replace(
# 	day=21, 
# 	month=7, 
# 	year=2021, 
# 	hour=18, 
# 	minute=15)
# ).save()

#FF0000