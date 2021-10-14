from django.contrib.auth import get_user_model

from rest_framework import (
    viewsets
)
from api.permissions import CanReadTableContent
User = get_user_model()


from tables.models import (
    Particip
)
from api.serializer import (
    UserSerializer, 
)

from .utils import (
    get_table_url
)


class User_in_table_view(viewsets.ModelViewSet):
    "show all users in table "
    "according to the url" 
    
    serializer_class = UserSerializer
    lookup_field = 'username' 
    permission_classes = [CanReadTableContent]
    http_method_names = ['get']

    
    def get_queryset(self):
        url = get_table_url(self.request.path)
        print(url)
        print(url)
        print(url)
        queryset = Particip.objects.select_related().filter(table_id__url=url)
        return queryset

