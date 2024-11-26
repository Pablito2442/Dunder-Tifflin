import braintree.client_token
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Pedido, DetallePedido
from producto.models import Producto
import braintree
import mysite.settings as settings

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
            braintree.Environment.Sandbox,
            merchant_id= settings.BRAINTREE_MERCHANT_ID, # "kxsttcxndt4cz2bm",
            public_key=settings.BRAINTREE_PUBLIC_KEY, # "p75tvtfx3tgr9z8w",
            private_key= settings.BRAINTREE_PRIVATE_KEY,#"a42231b58bd05dda4faaf787614c05a2"
        )
    )

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
        pedido = Pedido(
            cliente=request.user if request.user.is_authenticated else None,
            correo_cliente=correo_cliente if not request.user.is_authenticated else None,
            direccion_envio=direccion_envio,
            metodo_pago=metodo_pago,
            total=0,  # Se calculará después
        )

        total = 0
        detalles_pedido = []
        productos_modificados = []
        for producto_id, item in carrito.items():
            producto = Producto.objects.get(id=producto_id)
            subtotal = item['cantidad'] * item['precio']

            # Crear detalle del pedido
            detalles_pedido.append(DetallePedido(
                pedido=pedido,
                producto=producto,
                cantidad=item['cantidad'],
                precio_unitario=item['precio']
            ))

            # Actualizar stock del producto
            producto.stock -= item['cantidad']
            productos_modificados.append(producto)

            total += subtotal

        # Actualizar el total del pedido
        pedido.total = total

        if (metodo_pago == 'tarjeta'):
            nonce = request.POST['payment_method_nonce']

            result = gateway.transaction.sale({
                'amount': str(total),
                'payment_method_nonce': nonce,
                'options': {
                    'submit_for_settlement': True
                }
            })

            if not result.is_success:
                return redirect(reverse('finalizar_pedido')+"?transaction_error")

        # Guardar todas las entidades una vez se complete la transaccion con exito
        pedido.save()
        DetallePedido.objects.bulk_create(detalles_pedido)
        Producto.objects.bulk_update(productos_modificados, ['stock'])

        # Vaciar el carrito después de crear el pedido
        del request.session['carrito']

        return redirect('seguimiento_pedido', pedido_id=pedido.id)

    client_token = gateway.client_token.generate({})

    error=None
    if 'transaction_error' in request.GET:
        error='Hubo un error en la transacción'

    return render(request, 'pedido/finalizar_pedido.html', {'client_token':client_token, 'error': error})