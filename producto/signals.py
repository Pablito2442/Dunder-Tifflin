from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import *

@receiver(pre_save, sender=Producto)
def set_agotado(sender, instance, **kwargs):
    # Automatically set agotado based on cantidad_en_stock
    instance.agotado = instance.cantidad_en_stock == 0
