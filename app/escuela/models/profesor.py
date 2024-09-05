from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
