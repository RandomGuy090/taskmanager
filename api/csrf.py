from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import permissions
from django.middleware.csrf import get_token



# @method_decorator(ensure_csrf_cookie, name='dispatch')
class Get_csrf(APIView):

    def get(self, request, format=None):
        print("get")
        return Response({ 'success': 'CSRF cookie set'})
