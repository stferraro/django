from django.db import models
from .profesor import Profesor

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=200)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"