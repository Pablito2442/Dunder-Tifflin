"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Rutas para el panel de informacion general
    path('', views.panel_informacion_general, name='panel_usuario'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('actualizar_usuario/', views.modificar_informacion_usuario, name='actualizar_usuario'),
    path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    
    # Rutas para el panel de pedidos
    path('pedidos/', views.panel_pedidos, name='panel_usuario_pedidos'),
    path('actualizar/<int:pedido_id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('detalle_pedido/', views.panel_pedidos, name='detalle_pedido'),
    
    # Rutas para el panel de administración de usuarios
    path('administracion_usuarios/', views.panel_tablas_usuarios_administracion, name='panel_administracion_usuarios'),
    path('modificar_usuario/', views.modificar_usuario_administrados, name='modificar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('anadir_usuario/', views.anadir_usuario, name='anadir_usuario'),
    
    # Rutas para el panel de administracion de productos
    path('administracion_productos/', views.panel_tablas_productos_administracion, name='panel_administracion_productos'),
    path('actualizar_producto/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/', views.eliminar_producto, name='eliminar_producto'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    
    path('actualizar_fabricante/', views.actualizar_fabricante, name='actualizar_fabricante'),
    path('eliminar_fabricante/', views.eliminar_fabricante, name='eliminar_fabricante'),
    path('crear_fabricante/', views.crear_fabricante, name='crear_fabricante'),
    
    path('actualizar_categoria/', views.actualizar_categoria, name='actualizar_categoria'),
    path('eliminar_categoria/', views.eliminar_categoria, name='eliminar_categoria'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    
    # Rutas para el panel de administracion de pedidos
    path('administracion_pedidos/', views.panel_tablas_pedidos_administracion, name='panel_administracion_pedidos'),
    path('modificar_pedido/', views.modificar_pedidos, name='modificar_pedido'),
    path('eliminar_pedido/', views.eliminar_pedidos, name='eliminar_pedido'),
    path('modificar_detalles_pedidos/', views.modificar_detalles_pedidos, name='modificar_detalles_pedidos'),
    path('eliminar_detalles_pedidos/', views.eliminar_detalles_pedidos, name='eliminar_detalles_pedidos'),
    
]
