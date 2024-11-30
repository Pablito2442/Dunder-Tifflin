from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Producto, Categoria, Fabricante

# Listar productos por categoría o fabricante
def listar_productos(request, categoria_id=None, fabricante_id=None):
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    productos = Producto.objects.filter(agotado=False, cantidad_en_stock__gt=0)  # Solo productos disponibles
    agotados = Producto.objects.filter(Q(agotado=True) | Q(cantidad_en_stock=0))

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    if fabricante_id:
        productos = productos.filter(fabricante_id=fabricante_id)

    return render(request, 'producto/catalogo.html', {
        'productos': productos,
        'agotados' : agotados,
        'categorias': categorias,
        'fabricantes': fabricantes,
        'categoria_actual': categoria_id,
        'fabricante_actual': fabricante_id,
    })

# Ficha de producto
def ficha_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto/ficha_producto.html', {'producto': producto})
