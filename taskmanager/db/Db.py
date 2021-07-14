from django.db import models
#to get from taskmanager.Db import ToDoList, Item

class User(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	singupDate = models.DateTimeField(auto_now_add=True, blank=True)

class Tables(models.Model):
	name = models.CharField(max_length=100)

class Particip(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)

