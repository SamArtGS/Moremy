from django.contrib import admin
from django.urls import path

from .views import *

app_name = "cursos_app"

urlpatterns = [
  path("api/listCursos", CursoList.as_view(), name="list_cursos"),
]
