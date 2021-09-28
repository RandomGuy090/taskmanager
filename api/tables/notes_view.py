
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


class Notes_view(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "added_date"
    permission_classes = [CanReadTableContent]

    def get_queryset(self):
        url = get_table_url(self.request.path)
        queryset = Notes.objects.select_related().filter(table_id__url=url)
        return queryset