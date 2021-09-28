from django.core import serializers

from tables.models import Notes, Tables, Particip, Task_color
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, login





User = get_user_model()

class NotesSerializer(serializers.ModelSerializer):
	table_id = serializers.SlugRelatedField(queryset=Tables.objects.all(), slug_field='url')
	user_id= serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	lookup_field = "id"

	class Meta:
		model = Notes
		fields = "__all__"


class TablesSerializer(serializers.ModelSerializer):    
	class Meta:        
		model = Tables     
		exclude = ["password"]



class UserSerializer(serializers.ModelSerializer):  
	table_id = serializers.SlugRelatedField(queryset=Tables.objects.all(), slug_field='url')
	user_id= serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	lookup_field= "id"

	class Meta:        
		model = Particip      
		fields = "__all__"
