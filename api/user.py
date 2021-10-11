from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponseServerError, JsonResponse
from taskmanager.exceptions import NotLogged
from rest_framework import (
    viewsets
)

User = get_user_model()


from tables.models import (
    Tables
)

from api.serializer import (
    TablesCreateSerializer,
    UserInfo
)

from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator


@method_decorator(ensure_csrf_cookie, name="dispatch")
class User_username_view(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfo

    def list(self, request):
        "show logged user"
    
        user = self.request.session.get("username")
        queryset = self.queryset.filter(username=user)
        print(queryset)
        if len(queryset) == 0:

            res={
            "detail":"no info"
            }
            # raise NotLogged
            return JsonResponse(res)

        # return queryset
        res={
            "detail":"no info",
            "username":user,
            }
        return JsonResponse(res)


