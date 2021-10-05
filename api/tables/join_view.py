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
    Unauthorized
)


class Join_table(viewsets.ModelViewSet):

    
    serializer_class = TablesCreateSerializer
    lookup_field = 'id' 
    queryset = Tables.objects.all()
    http_method_names = ['post']



    def create(self, request, *args, **kwargs):
        "join new table via post"
        print("+++++++")
        try:
            password = self.request.POST.get("password")
        except:
            password = ""
        # password = self.request.query_params.get("password")
        url = get_table_url(self.request.path)
        user = self.request.session.get("username")

        part = Particip.objects.filter(user_id__username=user,
                                table_id__url=url)

        if part.exists():
            print("redirect")
            return HttpResponseRedirect(redirect_to=f'/api/tables/{url}') 

        qr = Tables.objects.filter(url=url).first()
        if qr == None:
            raise Unauthorized()

        if password == qr.password:
            if not request.POST._mutable:
                request.POST._mutable = True

            request.data["user_id"] = User.objects.filter(username=user).first().id
            request.data["table_id"] = Tables.objects.filter(url=url).first().id
            request.data.pop("password")

            serializer = self.serializer_class(data=self.request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                raise ServerError()
        else:
            raise PassowordNeeded()
        
        return Response("leaving")

        
        return Response(self.request.POST)
