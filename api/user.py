from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponseServerError

from rest_framework import (
    viewsets
)

User = get_user_model()


from tables.models import (
    Tables
)

from api.serializer import (
    TablesCreateSerializer
)


class User_username_view(viewsets.ViewSet):

    queryset=Tables.objects.all()
    

    def list(self, request, *args, **kwargs):
        "show logged user"

        
        user = self.request.session.get("username")
        asd = {"username": user}
        return Response(asd)


