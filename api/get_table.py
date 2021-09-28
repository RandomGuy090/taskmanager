
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth import get_user_model

from rest_framework import (
    routers, 
    serializers, 
    viewsets
)
from rest_framework.permissions import IsAuthenticated

from taskmanager.exceptions import (
    ServiceUnavailable,
    Unauthorized,
    NotAdded,
)
from tables.models import (
    Notes, 
    Tables, 
    Particip
)
from .serializer import (
    TablesSerializer, 
    UserSerializer, 
    NotesSerializer
)


from .permissions import CanReadTableContent
User = get_user_model()

"""

"""

def get_table_url(path):
    "gets tbl_id from /api/tables/tbl_id/users"
    url = path
    if url.endswith("/"):
        url=url[:-1]
    url = url.split("/")
    url = url[url.index(url[-1])-1]
    return url

class NotesView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "added_date"
    permission_classes = [CanReadTableContent]

    def get_queryset(self):
        url = get_table_url(self.request.path)
        queryset = Notes.objects.select_related().filter(table_id__url=url)
        return queryset

class UserInTableView(viewsets.ModelViewSet):
    "show all users in table "
    "according to the url" 
    
    serializer_class = UserSerializer
    lookup_field = 'username' 
    # permission_classes = [IsAuthenticated]
    permission_classes = [CanReadTableContent]
    
    def get_queryset(self):

        url = get_table_url(self.request.path)

        queryset = Particip.objects.select_related().filter(table_id__url=url)

        return queryset


class TableView(viewsets.ModelViewSet):
    "list all tables"
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
    lookup_field = "url"

    # def get_querryset(self):
    def table_data(self):
        print("TABLES_DATA")
        queryset = Particip.objects.select_related("user_id")
        queryset = queryset.filter(user_id__username=username)



    # def get_queryset(self):
    #     username = self.request.session.get("username")
    #     print(username)
    #     print(username)
    #     print(username)
    #     queryset = Particip.objects.select_related("user_id")
    #     queryset = queryset.filter(user_id__username=username)
    #     return queryset
