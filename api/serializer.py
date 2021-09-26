from django.core import serializers

from tables.models import Notes, Tables, Particip, Task_color
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, login





User = get_user_model()

class NotesSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='user-detail', source='profile',)

	class Meta:
		model = Notes
		fields = "__all__"
		# fields = ['user_id', 'table_id', 'table_note', 'added_date', 'todo_date_start', 'todo_date_end']

class TablesSerializer(serializers.ModelSerializer):    
	class Meta:        
		model = Tables     
		exclude = ["password"]



class UserSerializer(serializers.ModelSerializer):  
	table_id = serializers.SlugRelatedField(queryset=Tables.objects.all(), slug_field='url')
	user_id= serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

	class Meta:        
		model = Particip      
		fields = "__all__"
