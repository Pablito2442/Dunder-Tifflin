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
    
    # Rutas para el panel de pagos
    path('pagos/', views.panel_pagos, name='panel_usuario_pagos'),
    
    
    # Rutas para el panel de administración de usuarios
    path('administracion_usuarios/', views.panel_tablas_usuarios_administracion, name='panel_administracion_usuarios'),
    path('modificar_usuario/', views.modificar_usuario_administrados, name='modificar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('anadir_usuario/', views.anadir_usuario, name='anadir_usuario'),
    
    # Rutas para el panel de administracion de productos
    path('administracion_productos/', views.panel_tablas_productos_administracion, name='panel_administracion_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    
    path('administracion_pedidos/', views.panel_tablas_pedidos_administracion, name='panel_administracion_pedidos'),
    
    path('administracion_pagos/', views.panel_tablas_pagos_administracion, name='panel_administracion_pagos'),
    
]
