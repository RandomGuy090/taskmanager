from django.db import models
#to get from taskmanager._db import _to_do_list, _item
import random
from datetime import datetime
def gen_url(lenght=16):
	rstr = ""
	for _ in range(lenght):
	    integ = random.randint(97, 97 + 26 - 1)
	    rstr += (chr(integ))
	return rstr


class User(models.Model):
	name = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	singup_date = models.DateTimeField(auto_now_add=True, blank=True)
	prof_img = models.CharField(max_length=100, default="/img/profile.png")



class Tables(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=16, default=gen_url)
	color = models.CharField(max_length=7, default="#_b5_e61")
	border_color = models.CharField(max_length=7)
	password = models.CharField(max_length=200, default="")
	password_needed = models.BooleanField(default=False)

class Task_color(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	table_id = models.ForeignKey(Tables, on_delete=models.CASCADE)
	color = models.CharField(max_length=7, default="")

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


	

# db._notes(
# user_id=db.User.objects.get(name="admin"),
# table_id=db.Tables.objects.get(name="testing1"),
# table_note="testing note2",
# todo_date=datetime.strptime("","").replace(
# 	day=21, 
# 	month=7, 
# 	year=2021, 
# 	hour=18, 
# 	minute=15)
# ).save()

#_ff0000