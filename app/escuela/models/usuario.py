from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=200)
    rol = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username

