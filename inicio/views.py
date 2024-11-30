from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from producto.models import *

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def search_results(request):
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()

    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria_id')
    fabricante_id = request.GET.get('fabricante_id')

    results =  Producto.objects.all()
    if query:
        results = results.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    if categoria_id:
        results = results.filter(categoria_id=categoria_id)

    if fabricante_id:
        results = results.filter(fabricante_id=fabricante_id)

    return render(request, 'search_results.html', {
        'results': results,
        'categorias': categorias,
        'fabricantes': fabricantes,
        'categoria_id': categoria_id,
        'fabricante_id': fabricante_id,
        'query': query
    })

def contacto(request):
    return render(request, 'contacto.html')