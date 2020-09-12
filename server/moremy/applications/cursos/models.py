from django.db import models

PROGRESO_CHOICES = [
  ("P", "Por Iniciar"),
  ("C", "En Curso"),
  ("F", "Finalizado"),
]


class Curso(models.Model):
  nombre = models.CharField("Nombre", max_length=50)
  descripcion = models.CharField("Descripción", max_length=255)
  disponible = models.BooleanField()


class Modulo(models.Model):
  nombre = models.CharField("Nombre", max_length=50)
  descripcion = models.CharField("Descripción", max_length=50)
  nivel_dificultad = models.IntegerField()
  ultima_actualizacion = models.DateField(
    "Ultima actualización", auto_now=False, auto_now_add=False
  )
  duracion = models.DecimalField("Duración", max_digits=6, decimal_places=2)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  status_progreso = models.CharField(
    "Status de Progreso", max_length=1, choices=PROGRESO_CHOICES
  )
