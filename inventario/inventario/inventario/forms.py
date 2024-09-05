from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models.user import CustomUser
from .models.product import Product

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'role')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']  # Campos del formulario
