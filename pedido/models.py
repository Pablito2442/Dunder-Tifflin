from django.db import models
from django.contrib.auth.models import User
from producto.models import Producto

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('procesado', 'Procesado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    correo_cliente = models.EmailField(blank=True, null=True)  # Correo para usuarios no registrados
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    direccion_envio = models.TextField()
    metodo_pago = models.CharField(max_length=50, default='contrareembolso')  # Ejemplo: contrareembolso, tarjeta
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.estado}"

    def total_pedido(self):
        """
        Calcula el total del pedido sumando los subtotales de los detalles.
        """
        return sum(detalle.subtotal() for detalle in self.detalles.all())


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        """
        Calcula el subtotal de este detalle del pedido.
        """
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Pedido #{self.pedido.id})"
