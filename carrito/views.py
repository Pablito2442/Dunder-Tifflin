from django.shortcuts import render, redirect, get_object_or_404
from producto.models import Producto
from pedido.models import Pedido, DetallePedido

# Agregar un producto al carrito
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    else:
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1,
        }

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

# Ver el contenido del carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito/carrito.html', {'carrito': carrito, 'total': total})

# Incrementar cantidad
def incrementar_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

# Reducir cantidad
def reducir_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        if carrito[str(producto_id)]['cantidad'] > 1:
            carrito[str(producto_id)]['cantidad'] -= 1
        else:
            del carrito[str(producto_id)]
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

# Vaciar el carrito
def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('ver_carrito')
