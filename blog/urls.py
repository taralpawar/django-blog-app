
from django.urls import path, include

from .views import homepage, newpost, loginuser, register, logoutuser, readblog, searchblog, mypost

urlpatterns = [

    path('home', homepage),
    path('newpost', newpost),

    path('login', loginuser),
    path('register', register),
    path('logout', logoutuser),
    path('read/<int:id>/', readblog),
    path('search', searchblog),
    path('mypost', mypost)
]
