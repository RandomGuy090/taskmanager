from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponseServerError, JsonResponse

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

import json

class Join_table(viewsets.ModelViewSet):

    
    serializer_class = TablesCreateSerializer
    lookup_field = 'id' 
    queryset = Tables.objects.all()
    http_method_names = ['post']



    def create(self, request, *args, **kwargs):

        print(self.request.session.items())
        print(dir(self.request.session))
        print(request.session.get("username"))
        # return JsonResponse({
        #     "asdf":"asdf"
        #     })

        "join new table via post"
        print("+++++++")
        data = self.request.body
        data = data.decode("utf-8")
        data = json.loads(data)
        print(data)

        try:
            password = data.get("password")
        except:
            password = ""
        print(password)
        # password = self.request.query_params.get("password")
        url = get_table_url(self.request.path)
        # user = self.request.session.get("username")
        user = self.request.user.username

        print(request.user.is_authenticated)
        print(user)

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
            print(data)
            print(data)
            data["user_id"] = User.objects.filter(username=user).first().id
            data["table_id"] = Tables.objects.filter(url=url).first().id
            data.pop("password")
         
            serializer = self.serializer_class(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                raise ServerError()
        else:
            raise PassowordNeeded()
        
        return Response("leaving")

        
        return Response(self.request.POST)
