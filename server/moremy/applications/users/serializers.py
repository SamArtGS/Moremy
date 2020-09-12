from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserTokenSerializer(serializers.Serializer):
  token_id = serializers.CharField(required=True)


class UserSerializer(serializers.Serializer):
  username = serializers.CharField()
  nombre = serializers.CharField()
  ap_paterno = serializers.CharField()
  ap_materno = serializers.CharField()
  password = serializers.CharField()

  def validate_username(self, data):
    user = User.objects.filter(username=data)
    if user.count() != 0:
      raise serializers.ValidationError("El nombre de Usuario ya existe")
    return data


class LoginSerializer(serializers.Serializer):
  token = serializers.CharField(read_only=True)
  nombre = serializers.CharField(read_only=True)
  ap_paterno = serializers.CharField(read_only=True)
  ap_materno = serializers.CharField(read_only=True)
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    super().validate(data)
    usuario = authenticate(
      username=data.get("username"),
      password=data.get("password"),
    )
    if not usuario:
      raise serializers.ValidationError(
        "El usuario o contraseña no son validos"
      )
    data["token"] = Token.objects.get(user=usuario)
    data["nombre"] = usuario.nombre
    data["ap_paterno"] = usuario.ap_paterno
    data["ap_materno"] = usuario.ap_materno
    return data
