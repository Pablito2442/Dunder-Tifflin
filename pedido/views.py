from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, DetallePedido
from producto.models import Producto

# Ver el estado de un pedido por su ID
def seguimiento_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedido/seguimiento.html', {'pedido': pedido})

# Crear un pedido desde el carrito
def finalizar_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        return redirect('ver_carrito')

    if request.method == 'POST':
        direccion_envio = request.POST['direccion_envio']
        metodo_pago = request.POST['metodo_pago']
        correo_cliente = request.POST.get('correo_cliente', None)  # Captura del correo

        # Crear el pedido
        pedido = Pedido.objects.create(
            cliente=request.user if request.user.is_authenticated else None,
            correo_cliente=correo_cliente if not request.user.is_authenticated else None,
            direccion_envio=direccion_envio,
            metodo_pago=metodo_pago,
            total=0,  # Se calculará después
        )

        total = 0
        for producto_id, item in carrito.items():
            producto = Producto.objects.get(id=producto_id)
            subtotal = item['cantidad'] * item['precio']

            # Crear detalle del pedido
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=item['cantidad'],
                precio_unitario=item['precio']
            )

            # Actualizar stock del producto
            producto.stock -= item['cantidad']
            producto.save()

            total += subtotal

        # Actualizar el total del pedido
        pedido.total = total
        pedido.save()

        # Vaciar el carrito después de crear el pedido
        del request.session['carrito']

        return redirect('seguimiento_pedido', pedido_id=pedido.id)

    return render(request, 'pedido/finalizar_pedido.html')
