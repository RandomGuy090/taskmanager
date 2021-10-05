from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponseServerError

from rest_framework import (
    viewsets
)
from api.permissions import CanReadTableContent
User = get_user_model()


from tables.models import (
    Particip,
    Tables
)

from .utils import (
    get_table_url
)

from api.serializer import (
    UserSerializer, 
    TablesSerializerList, 
    TablesSerializerDetail,
    TablesCreateSerializer
)

from taskmanager.exceptions import (
    ServerError,
    PassowordNeeded,
    NoSuchTable,
    LeftTable,
)

class Leave_table(viewsets.ModelViewSet):


    serializer_class = TablesCreateSerializer
    lookup_field = 'id' 
    queryset = Tables.objects.all()
    http_method_names = ['post']

    permission_classes = [CanReadTableContent]
    

    def create(self, request, *args, **kwargs):
        "join new table via post"
        print("+++++++")
        url = get_table_url(self.request.path)
        user = self.request.session.get("username")

        part = Particip.objects.filter(user_id__username=user,
                                table_id__url=url)

        if part.exists():
            part.delete()
            raise LeftTable()
        else:
            raise NoSuchTable()



