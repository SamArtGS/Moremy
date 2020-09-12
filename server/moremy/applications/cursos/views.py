from django.shortcuts import render
from rest_framework.generics import (
  CreateAPIView,
  DestroyAPIView,
  ListAPIView,
  RetrieveAPIView,
  RetrieveUpdateAPIView,
  UpdateAPIView,
)

from .models import Curso, Modulo
from .serializers import CursoSerializer


class CursoList(ListAPIView):
  serializer_class = CursoSerializer

  def get_queryset(self):
    return Curso.objects.all()
