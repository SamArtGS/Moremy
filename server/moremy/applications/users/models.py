from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

#
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

  username = models.CharField("Nombre de Usuario", max_length=50, unique=True)
  nombre = models.CharField("Nombre(s)", max_length=50)
  ap_paterno = models.CharField("Apellido Paterno", max_length=50)
  ap_materno = models.CharField(
    "Apellido Materno", max_length=50, null=True, blank=True
  )
  #
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)

  USERNAME_FIELD = "username"

  REQUIRED_FIELDS = ["nombre", "ap_paterno"]

  objects = UserManager()

  def get_short_name(self):
    return self.nombre

  def get_full_name(self):
    return self.full_name
