"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views.auth_views import register, CustomLoginView  # Importamos vistas de autenticación
from .views.home_views import home  # Importamos vista home
from .views.product_views import add_product, list_products, delete_product, edit_product  # Importamos vistas de productos

urlpatterns = [
    path('', home, name='home'),  # Página de inicio para usuarios autenticados
    path('register/', register, name='register'),  # Página de registro
    path('login/', CustomLoginView.as_view(), name='login'),
    path('add-product/', add_product, name='add_product'),  # URL para agregar producto
    path('list-products/', list_products, name='list_products'),  # URL para listar productos
    path('add-product/', add_product, name='add_product'),  # URL para agregar productos
    path('list-products/', list_products, name='list_products'),  # URL para listar productos
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),  # URL para eliminar productos
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # URL para cerrar sesión
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),  # URL para eliminar productos
    path('edit-product/<int:product_id>/', edit_product, name='edit_product'),  # URL para modificar productos
]  








