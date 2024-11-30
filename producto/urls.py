from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='catalogo'),  # Lista todos los productos
    path('producto/<int:producto_id>/', views.ficha_producto, name='ficha_producto'),  # Ver detalles de un producto
]
