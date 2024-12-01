from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración de Django
    
    path('', RedirectView.as_view(url='/inicio/', permanent=True)),  # Redirección a inicio
    
    path('inicio/', include('inicio.urls')),  # Panel de pagina inicial
    
    path('login/', include('login.urls')),  # Panel de login y registro
    path('usuario/', include('usuario.urls')),  # Panel de administración del usuario
        
    path('productos/', include('producto.urls')),  # Rutas de productos
    path('carrito/', include('carrito.urls')),  # Rutas de carrito
    path('pedidos/', include('pedido.urls')),  # Rutas de pedidos    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)