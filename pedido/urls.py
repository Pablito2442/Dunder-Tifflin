from django.urls import path
from . import views

urlpatterns = [
    path('finalizar/', views.finalizar_pedido, name='finalizar_pedido'),  # Finalizar un pedido
    path('seguimiento/<str:codigo_seguimiento>/', views.seguimiento_pedido, name='seguimiento_pedido'),
]
