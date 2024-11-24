from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración de Django
    
    path('inicio/', include('inicio.urls')),  # Panel de pagina inicial
    
    path('login/', include('login.urls')),  # Panel de login y registro
    path('usuario/', include('usuario.urls')),  # Panel de administración del usuario
        
    path('productos/', include('producto.urls')),  # Rutas de productos
    path('carrito/', include('carrito.urls')),  # Rutas de carrito
    path('pedidos/', include('pedido.urls')),  # Rutas de pedidos
]