"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from account.logout.views import Logout


from account.login.views import Login
from account.register.views import Register
from landingpage.views import LandingPage
from tables.views import Tables

urlpatterns = [
    path('admin/', admin.site.urls , name='admin'),
    path('logout/', Logout.as_view(), name='logout_route'),
    path('login/', Login.as_view(), name="login_route"),
    path('register/', Register.as_view(), name="register_route"),
    path('tables/<str:table_id>', Tables.as_view(), name="tables_url"),
    path('tables/', Tables.as_view(), name="tables_route"),
    path("", login_required(LandingPage.as_view(), login_url="/login/?next=/"), name="landingpage_route"),
    path("api/", include("api.urls"))
]



