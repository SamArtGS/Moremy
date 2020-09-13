from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

#
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=50, unique=True)
  nombre = models.CharField(max_length=50)
  ap_paterno = models.CharField(max_length=50)
  ap_materno = models.CharField(max_length=50, null=True, blank=True)
  is_student = models.BooleanField(default=True)
  is_instructor = models.BooleanField(default=False)

  #
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  USERNAME_FIELD = "username"
  REQUIRED_FIELDS = ["nombre", "ap_paterno"]
  objects = UserManager()

  def get_profile(self):
    if self.is_student:
      return "student"
    return "instructor"


class StudentProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  curp = models.CharField(max_length=18, null=True)
  telefono = models.CharField(max_length=15, null=True)
  fecha_nacimiento = models.DateField(null=True)
  email = models.EmailField(null=True)
  foto = models.ImageField(null=True)
