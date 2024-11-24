from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='catalogo'),  # Lista todos los productos
    path('categoria/<int:categoria_id>/', views.listar_productos, name='productos_por_categoria'),  # Filtrar por categoría
    path('fabricante/<int:fabricante_id>/', views.listar_productos, name='productos_por_fabricante'),  # Filtrar por fabricante
    path('producto/<int:producto_id>/', views.ficha_producto, name='ficha_producto'),  # Ver detalles de un producto
]
