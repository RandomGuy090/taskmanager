
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
from api.permissions import CanReadTableContent
User = get_user_model()

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
from api.serializer import (
    TablesSerializer, 
    UserSerializer, 
    NotesSerializer
)
from .utils import (
    get_table_url
)



class Table_view(viewsets.ModelViewSet):
    "list all tables"
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
    lookup_field = "url"
