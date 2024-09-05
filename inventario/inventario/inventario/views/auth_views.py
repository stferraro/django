from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from ..forms import CustomUserCreationForm

# Vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario, pero no inicia sesión automáticamente
            return redirect('login')  # Redirige al login después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})

# Vista para el login de usuarios (usando la vista genérica de Django)
class CustomLoginView(LoginView):
    template_name = 'app/login.html'  # Plantilla que usa la vista para el login
    redirect_authenticated_user = True  # Redirige a la página de inicio si ya está autenticado

def custom_logout(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página de login







