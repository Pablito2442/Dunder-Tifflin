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
    rango_precio = request.GET.get('rango_precio')
    en_stock = request.GET.get('en_stock')

    results =  Producto.objects.all()
    if query:
        results = results.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    if categoria_id:
        results = results.filter(categoria_id=categoria_id)

    if fabricante_id:
        results = results.filter(fabricante_id=fabricante_id)

    if rango_precio:
        if rango_precio == '0-30':
            results = results.filter(precio__lt=30)
        elif rango_precio == '30-50':
            results = results.filter(precio__gte=30, precio__lt=50)
        elif rango_precio == '50-75':
            results = results.filter(precio__gte=50, precio__lt=75)
        elif rango_precio == '75-100':
            results = results.filter(precio__gte=75, precio__lt=100)
        elif rango_precio == '100-150':
            results = results.filter(precio__gte=100, precio__lt=150)
        elif rango_precio == '150-200':
            results = results.filter(precio__gte=150, precio__lt=200)
        elif rango_precio == '200':
            results = results.filter(precio__gte=200)

    if en_stock:
        results = results.filter(agotado=False)

    return render(request, 'search_results.html', {
        'results': results,
        'categorias': categorias,
        'fabricantes': fabricantes,
        'categoria_id': categoria_id,
        'fabricante_id': fabricante_id,
        'rango_precio': rango_precio,
        'en_stock': en_stock,
        'query': query
    })

def contacto(request):
    return render(request, 'contacto.html')