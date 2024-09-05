from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vista de inicio (solo para usuarios autenticados)
@login_required
def home(request):
    return render(request, 'app/home.html')
