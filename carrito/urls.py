from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),  # Ver el carrito
    path('agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),  # Agregar producto al carrito
    path('incrementar/<int:producto_id>/', views.incrementar_cantidad, name='incrementar_cantidad'),  # Incrementar cantidad
    path('reducir/<int:producto_id>/', views.reducir_cantidad, name='reducir_cantidad'),  # Reducir cantidad
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),  # Vaciar carrito
]
