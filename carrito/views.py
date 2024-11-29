import json
from pyexpat.errors import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import producto
from producto.models import Producto
from pedido.models import Pedido, DetallePedido

# Agregar un producto al carrito
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    if request.method == 'POST':
        data = request.body
        data = data.decode('utf-8')
        data = json.loads(data)
        cantidad = int(data.get('cantidad'))
    else:
        cantidad = 1

    if producto.agotado or producto.cantidad_en_stock == 0:
        messages.error(request, "El producto no está disponible en este momento.")
        return redirect('ver_carrito')

    if str(producto_id) in carrito:
        if producto.cantidad_en_stock >= carrito[str(producto_id)]['cantidad'] + cantidad:
            carrito[str(producto_id)]['cantidad'] += cantidad
        else:
            messages.error(request, "No hay suficiente stock disponible.")

    else:
        if producto.cantidad_en_stock >= cantidad:
            carrito[str(producto_id)] = {
                'nombre': producto.nombre,
                'precio': float(producto.precio),
                'cantidad': cantidad,
            }
        else:
            messages.error(request, "No hay suficiente stock disponible.")

    request.session['carrito'] = carrito

    if request.method == 'POST':
        return JsonResponse({})
    return redirect('ver_carrito')

# Ver el contenido del carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())

    # Calcular gastos de envío
    if total < 60:
        gastos_envio = 6.99
    else:
        gastos_envio = 0.0

    total_con_envio = total + gastos_envio

    return render(request, 'carrito/carrito.html', {
        'carrito': carrito,
        'total': total,
        'gastos_envio': gastos_envio,
        'total_con_envio': total_con_envio
    })
    
def incrementar_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto = get_object_or_404(Producto, id=producto_id)  # Obtener instancia del producto

    if str(producto_id) in carrito:
        if producto.cantidad_en_stock >= carrito[str(producto_id)]['cantidad'] + 1:
            carrito[str(producto_id)]['cantidad'] += 1
        else:
            messages.error(request, "No hay suficiente stock disponible para este producto.")
    else:
        messages.error(request, "El producto no está en el carrito.")

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

def eliminar_producto_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

# Vaciar el carrito
def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('ver_carrito')
