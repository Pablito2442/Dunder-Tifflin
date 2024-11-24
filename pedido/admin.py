from django.contrib import admin
from .models import Pedido, DetallePedido

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]
    list_display = ('id', 'cliente', 'correo_cliente', 'fecha', 'estado', 'total')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__username', 'correo_cliente')
