from django.urls import path, include
from django.contrib.auth import views as auth_views

from bases.views import Home, HomeSinPrivilegios

from .views import *


urlpatterns = [
    path('',Home.as_view(), name='home'),
    
]