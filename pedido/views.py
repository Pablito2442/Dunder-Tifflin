import braintree
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Pedido, DetallePedido
from producto.models import Producto
from django.contrib import messages
import mysite.settings as settings

# Configuración de Braintree
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY,
    )
)

# Seguimiento de un pedido por su ID
def seguimiento_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedido/seguimiento.html', {'pedido': pedido})


# Finalizar un pedido desde el carrito
def finalizar_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.error(request, "El carrito está vacío.")
        return redirect('ver_carrito')

    if request.method == 'POST':
        direccion_envio = request.POST.get('direccion_envio')
        metodo_pago = request.POST.get('metodo_pago')
        correo_cliente = request.POST.get('correo_cliente') if not request.user.is_authenticated else request.user.email

        if not direccion_envio:
            messages.error(request, "Debe proporcionar una dirección de envío.")
            return redirect('finalizar_pedido')

        # Crear instancia del pedido
        pedido = Pedido(
            cliente=request.user if request.user.is_authenticated else None,
            correo_cliente=correo_cliente,
            direccion_envio=direccion_envio,
            metodo_pago=metodo_pago,
            total=0,  # Calculado más adelante
            gastos_envio=0,  # Inicializar gastos de envío
        )

        total = 0
        detalles_pedido = []
        productos_modificados = []

        for producto_id, item in carrito.items():
            producto = get_object_or_404(Producto, id=producto_id)

            if producto.cantidad_en_stock < item['cantidad']:
                messages.error(request, f"No hay suficiente stock para el producto {producto.nombre}.")
                return redirect('ver_carrito')

            # Crear detalle del pedido
            detalles_pedido.append(DetallePedido(
                pedido=pedido,
                producto=producto,
                cantidad=item['cantidad'],
                precio_unitario=item['precio']
            ))

            # Actualizar stock del producto
            producto.cantidad_en_stock -= item['cantidad']
            if producto.cantidad_en_stock == 0:
                producto.agotado = True
            productos_modificados.append(producto)

            total += item['cantidad'] * item['precio']


        # Calcular gastos de envío
        if total < 60:
            pedido.gastos_envio = 6.99
        else:
            pedido.gastos_envio = 0
        
        # Actualizar el total del pedido
        pedido.total = total + pedido.gastos_envio
        pedido.subtotal=total

        # Manejo del pago si el método es tarjeta
        if metodo_pago == 'tarjeta':
            nonce = request.POST.get('payment_method_nonce')
            result = gateway.transaction.sale({
                'amount': str(total),
                'payment_method_nonce': nonce,
                'options': {'submit_for_settlement': True}
            })

            if not result.is_success:
                messages.error(request, "Error en la transacción. Intente nuevamente.")
                return redirect('finalizar_pedido')

        # Guardar pedido y sus detalles
        pedido.save()
        DetallePedido.objects.bulk_create(detalles_pedido)
        Producto.objects.bulk_update(productos_modificados, ['cantidad_en_stock', 'agotado'])

        # Enviar correo de confirmación
        enviar_correo_confirmacion(pedido)

        # Vaciar el carrito
        request.session['carrito'] = {}

        messages.success(request, f"Pedido #{pedido.id} creado con éxito.")
        return redirect('seguimiento_pedido', pedido_id=pedido.id)

    client_token = gateway.client_token.generate({})
    error = request.GET.get('transaction_error', None)

    return render(request, 'pedido/finalizar_pedido.html', {'client_token': client_token, 'error': error})


def enviar_correo_confirmacion(pedido):
    """
    Envía un correo de confirmación al cliente con los detalles del pedido.
    """
    base_url = "http://127.0.0.1:8000"  # Cambiar por el dominio en producción
    enlace_seguimiento = f"{base_url}{reverse('seguimiento_pedido', args=[pedido.id])}"

    detalles = pedido.detalles.all()
    mensaje = f"""
    Hola,

    Gracias por tu compra. Aquí están los detalles de tu pedido:

    Pedido ID: {pedido.id}
    Estado: {pedido.estado}
    Dirección de Envío: {pedido.direccion_envio}
    Método de Pago: {pedido.metodo_pago}

    Productos:
    """
    for detalle in detalles:
        mensaje += f"\t- {detalle.producto.nombre} (x{detalle.cantidad}): €{detalle.subtotal():.2f}\n"

    mensaje += f"""
    Gastos de Envío: €{pedido.gastos_envio:.2f}
    Total: €{pedido.total:.2f}

    Enlace para seguir tu pedido: {enlace_seguimiento}

    ¡Gracias por confiar en nosotros!
    """

    destinatario = pedido.correo_cliente
    send_mail(
        subject=f"Confirmación de tu Pedido #{pedido.id}",
        message=mensaje,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[destinatario],
        fail_silently=False,
    )
