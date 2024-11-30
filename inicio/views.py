from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from producto.models import *

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def search_results(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    return render(request, 'search_results.html', {'results': results, 'query': query})

def contacto(request):
    return render(request, 'contacto.html')