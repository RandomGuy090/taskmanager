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
from .tables.notes_view import (Notes_view
    )

from .tables.users_view import User_in_table_view

main_router = routers.SimpleRouter()
main_router.register(r"tables", Table_view, basename='api-tables')




users_router = routers.NestedSimpleRouter(main_router, r'tables', lookup='users')
users_router.register(r'users', User_in_table_view, basename="users_id")
users_router.register(r'notes', Notes_view, basename="users-detail")

app_name = "api"

urlpatterns = [
    path('',include(main_router.urls)),
    path('',include(users_router.urls)),

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
#                 add/
#                     <noteid>
#                 del/
#                     <noteid>
#             join/
#                 <userid>
#             leave/
#                 <userid>














