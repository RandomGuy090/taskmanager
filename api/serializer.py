from django.core import serializers

from tables.models import Notes, Tables, Particip, Task_color
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, login


User = get_user_model()

class NotesSerializer(serializers.ModelSerializer):
	"get all notes from table"

	table_id = serializers.SlugRelatedField(queryset=Tables.objects.all(), slug_field='url')
	user_id= serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	class Meta:
		model = Notes
		fields = "__all__"


class TablesSerializerList(serializers.ModelSerializer):    
	"get table info in list view"
	
	table_id = serializers.SlugRelatedField(queryset=Tables.objects.all(), slug_field='url')
	user_id= serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	class Meta:        
		model = Particip
		fields = "__all__"


class TablesSerializerDetail(serializers.ModelSerializer):    
	"get table info in detailed view"
	class Meta:        
		exclude = ["password"]
		# fields = "__all__"

		model = Tables


class UserSerializer(serializers.ModelSerializer):  
	"get all users added to the table"
	table_id = serializers.SlugRelatedField(queryset=Tables.objects.all(), slug_field='url')
	user_id= serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	lookup_field= "id"

	class Meta:        
		model = Particip      
		fields = "__all__"


class TablesCreateSerializer(serializers.ModelSerializer):    
	"get table info in detailed view"

	class Meta:        
		# exclude = ["url"]
		fields = "__all__"
		lookup_field = "id"
		model = Particip

