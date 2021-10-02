from django.contrib import admin
from .models import (
	Notes,
	Particip, 
	Task_color, 
	Tables
)
# Register your models here.
admin.site.register(Notes)
admin.site.register(Particip)
admin.site.register(Task_color)
admin.site.register(Tables)


