from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    BASIC = 'basic'
    
    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (BASIC, 'Basic User'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=BASIC)

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)  # Cambié a EmailField para mejor manejo de correos electrónicos
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Añade un related_name único
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Añade un related_name único
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

