from django.contrib import admin
from django.urls import path

from .views import *

app_name = "users_app"

urlpatterns = [
  path("api/users/register", UserRegister.as_view(), name="registerUser"),
  path("api/users/login", UserLogin.as_view(), name="loginUser"),
]
