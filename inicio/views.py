from django.http import HttpResponse
from django.shortcuts import render
from producto.models import Producto

def inicio(request):
    # Obtener productos destacados
    productos_destacados = Producto.objects.filter(destacado=True)
    return render(request, 'inicio.html', {'productos_destacados': productos_destacados})
