
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
)

from django.db.models.query import QuerySet

class Table_view(viewsets.ModelViewSet):
    "list all tables"
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
    lookup_field = "url"

    def get_queryset(self):
        user = self.request.session.get("username")
        # pr = Particip.objects.select_related().filter(user_id__username=user)
        pr = Particip.objects.raw("SELECT * FROM tables_particip GROUP BY table_id_id")
        return pr


