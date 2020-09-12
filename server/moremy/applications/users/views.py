from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import User
from .serializers import LoginSerializer, UserSerializer


class UserRegister(APIView):
  serializer_class = UserSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get("username")
    nombre = serializer.data.get("nombre")
    ap_paterno = serializer.data.get("ap_paterno")
    ap_materno = serializer.data.get("ap_materno")
    password = serializer.data.get("password")
    usuario = User.objects.create_user(
      username,
      password,
      nombre=nombre,
      ap_paterno=ap_paterno,
      ap_materno=ap_materno,
    )
    token = Token.objects.create(user=usuario)
    userGet = {
      "id": usuario.pk,
      "username": usuario.username,
      "nombre": usuario.nombre,
      "apellidos": usuario.ap_paterno + " " + str(usuario.ap_materno),
    }
    return Response({"token": token.key, "user": userGet})


class UserLogin(APIView):
  serializer_class = LoginSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
      return Response(serializer.data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
