from django.db import models
from .profesor import Profesor

class Materia(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=25)
    unidad_credito = models.CharField(max_length=5)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return self.nombre

