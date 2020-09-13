from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import StudentProfile, User


class UserTokenSerializer(serializers.Serializer):
  token_id = serializers.CharField(required=True)


class UserSerializer(serializers.Serializer):
  username = serializers.CharField()
  nombre = serializers.CharField()
  ap_paterno = serializers.CharField()
  ap_materno = serializers.CharField(required=False)
  password = serializers.CharField()
  email = serializers.EmailField(required=False)
  foto = serializers.ImageField(required=False)
  curp = serializers.CharField(required=False)
  telefono = serializers.CharField(required=False)
  fecha_nacimiento = serializers.DateField(required=False)

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
  rol = serializers.CharField(read_only=True)
  email = serializers.EmailField(read_only=True, required=False)
  foto = serializers.ImageField(read_only=True, required=False)
  telefono = serializers.CharField(read_only=True, required=False)
  username = serializers.CharField()
  password = serializers.CharField()

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
    data["rol"] = usuario.get_profile()
    if data["rol"] == "student":
      student = StudentProfile.objects.filter(user=usuario)
      if student.values("email"):
        data["email"] = student[0].email
      if student.values("telefono"):
        data["telefono"] = student[0].telefono
      if student.values("foto"):
        data["foto"] = student[0].foto
    return data
