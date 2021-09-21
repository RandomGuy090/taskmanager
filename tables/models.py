from django.db import models
import random
from datetime import datetime
from django.contrib import admin
from django.contrib.auth import get_user_model, authenticate, login
User = get_user_model()

def gen_color():
	ret = "#"
	for i in range(3):
		r = random.randrange(0, 255)
		r = hex(r)[2:]
		ret += r
	return ret

def make_border_color(color):
	if color.startswith("#"):
		color = color[1:]
	ret = "#"
	for elem in color:
		
		tmp = int(elem, 16) 
		tmp -=5
		if tmp < 0: tmp = 0
		ret+=str(hex(tmp)[2:])
	return ret



def gen_url(lenght=16):
	rstr = ""
	for _ in range(lenght):
		integ = random.randint(97, 97 + 26 - 1)
		rstr += (chr(integ))
	return rstr

class Tables(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=16, default=gen_url)
	color = models.CharField(max_length=7, default=gen_color)
	border_color = models.CharField(max_length=7, blank=True)
	password = models.CharField(max_length=200, default="", blank=True)
	# password_needed = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if not self.pk: # this will ensure that the object is new
			self.border_color = make_border_color(self.color)
		scuper().save(*args, **kwargs)



class Task_color(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	table_id = models.ForeignKey(Tables, on_delete=models.CASCADE)
	color = models.CharField(max_length=7, default=gen_color)

class Particip(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	table_id = models.ForeignKey(Tables, on_delete=models.CASCADE)
	color = models.ForeignKey(Task_color, on_delete=models.CASCADE)
	joined_date = models.DateTimeField(auto_now_add=True, blank=True)

class Notes(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	table_id = models.ForeignKey(Tables, on_delete=models.CASCADE)
	table_note = models.CharField(max_length=500, default="")
	added_date = models.DateTimeField(auto_now_add=True, blank=True)
	todo_date_start = models.DateTimeField(blank=True)
	todo_date_end = models.DateTimeField(blank=True)

admin.site.register(Notes)
admin.site.register(Particip)
admin.site.register(Task_color)
admin.site.register(Tables)


