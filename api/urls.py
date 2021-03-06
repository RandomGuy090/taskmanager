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

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# from rest_framework import routers
from rest_framework_nested import routers

from .tables.tables_view import Table_view
from .tables.notes_view import (Notes_view    )
from .tables.join_view import Join_table
from .tables.leave_view import Leave_table

from .tables.users_view import User_in_table_view


from .user import User_username_view


from .account.login.views import Login
from .account.login.tokenAuth import Token
from .account.register.views import Register
from .account.logout.views import Logout
from .csrf import Get_csrf

from rest_framework.authtoken.views import obtain_auth_token


main_router = routers.SimpleRouter()
main_router.register(r"tables", Table_view, basename='api-tables')


users_router = routers.NestedSimpleRouter(main_router, r'tables', lookup='users')
users_router.register(r'users', User_in_table_view, basename="users_id")
users_router.register(r'notes', Notes_view, basename="users-detail")

users_router.register(r'leave', Leave_table, basename="users-leave")
users_router.register(r'join', Join_table, basename="users-join")

app_name = "api"

urlpatterns = [
    path('',include(main_router.urls)),
    path('',include(users_router.urls)),
    path("user/", User_username_view.as_view({"get": "list"})),
    # path("login", UserLoginView.as_view({"post": "create"}))
    # path("login",include())
  
    path('logout/', Logout.as_view(), name='logout_route'),
    path('login/', Login.as_view(), name="login_route"),
    path('register/', Register.as_view(), name="register_route"),
    path('csrftoken/', Get_csrf.as_view(), name="csrftoken"),
    path('token/', obtain_auth_token),
]


# tables
# GET api/tables/<url>

#     GET get notes month
#     GET api/tables/<url>/notes/month/<month>

#     GET  get notes day
#     GET  api/tables/<url>/notes/days/<day>

# GET get user of table
# GET api/tables/url/users/

# create new table:
# POST api/tables/<url>

# add new user to table
# POST api/tables/<url>/users/<userid>

# add new note
# POST api/tables/<url>/notes/add/<noteid>

# delete note
# POST api/tables/<url>/notes/del/<noteid>

# join new table
# POST api/tables/<url>/join/<userid>

# leave table
# POST api/tables/<url>/leave/<userid>



# api/
#     tables/
#         <url>/
#             users/
#                 <userid>
#             notes/
#             join/
#                 <userid>
#             leave/
#                 <userid>














