from django.shortcuts import render
from django.contrib.auth.models import User

def panel_usuario(request):
    return render(request, 'index.html')

def panel_tablas(request):
    usuarios = User.objects.all()
    
    return render(request, 'table.html', {'usuarios': usuarios})
