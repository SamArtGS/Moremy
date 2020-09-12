from rest_framework import pagination, serializers

from .models import Curso, Modulo


class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = ("nombre", "descripcion", "disponible")
