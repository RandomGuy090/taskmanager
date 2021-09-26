
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth import get_user_model

from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated



from tables.models import Notes , Tables, Particip
from .serializer import TablesSerializer, UserSerializer, NotesSerializer

User = get_user_model()

class NotesView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class UserInTableView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = 'username' 
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):

        url = self.request.path
        if url.endswith("/"):
            url=url[:-1]
        url = url.split("/")
        url = url[url.index(url[-1])-1]
        queryset = Particip.objects.select_related().filter(table_id__url=url)

        return queryset


class TableView(viewsets.ModelViewSet):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
    lookup_field = "url"
