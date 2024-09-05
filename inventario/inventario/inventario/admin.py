from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from inventario.models.user import CustomUser
  # Asegúrate de que 'models' apunte al __init__.py que importa CustomUser

admin.site.register(CustomUser, UserAdmin)

