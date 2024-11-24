from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración de Django
    path('', include('producto.urls')),  # Rutas de productos (catálogo por defecto)
    path('carrito/', include('carrito.urls')),  # Rutas de carrito
    path('pedidos/', include('pedido.urls')),  # Rutas de pedidos
]