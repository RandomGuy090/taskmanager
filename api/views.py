
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from rest_framework import routers, serializers, viewsets
from django.contrib.auth import get_user_model, authenticate, login


from tables.models import Notes , Tables
from api.serializer import TablesSerializer, UserSerializer, NotesSerializer


# class NotesView(viewsets.ModelViewSet):
#     queryset = Notes.objects.all()
#     serializer_class = NotesSerializer


# class UserView(viewsets.ModelViewSet):
#     User = get_user_model()
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class TableView(viewsets.ModelViewSet):
#     queryset = Tables.objects.all()
#     serializer_class = TablesSerializer
