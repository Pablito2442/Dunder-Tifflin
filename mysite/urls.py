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
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('inicio.urls')),
    path('login/', include('login.urls')),
    path('usuario/', include('usuario.urls')),
    path('', views.listar_productos, name='catalogo'),
    path('categoria/<int:categoria_id>/', views.listar_productos, name='productos_por_categoria'),
    path('fabricante/<int:fabricante_id>/', views.listar_productos, name='productos_por_fabricante'),
    path('producto/<int:producto_id>/', views.ficha_producto, name='ficha_producto'),
    path('seguimiento/<int:pedido_id>/', views.seguimiento_pedido, name='seguimiento_pedido'),
    path('finalizar/', views.finalizar_pedido, name='finalizar_pedido'),
]

