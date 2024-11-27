from .countries import *
from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    phone_regex = r'^\+?(d{1,3})?(\s)?\d{9,15}$'
    if not re.match(phone_regex, value):
        raise ValidationError(f'{value} is not a valid phone number.')
    

class Fabricante(models.Model):
    """Representa el fabricante o la marca del producto."""
    nombre = models.CharField(unique=True, blank= False, null=False, max_length=100)
    descripcion = models.TextField(blank=True, null=True, max_length=1000)
    email = models.EmailField(unique=True, blank=True, null=True)
    numTlf = models.CharField(
        max_length=21,
        validators=[validate_phone_number],
        blank=True,
        null=True,
    )
    web = models.TextField(max_length=100, blank=True, null=True)
    pais = models.CharField(
        max_length=3,
        choices=Country.choices,
        default=Country.SPAIN
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fabricantes"
        ordering = ['nombre']


class Categoria(models.TextChoices):
    SILLAS = 'sillas', 'Sillas'
    ILUMINACION = 'iluminación', 'Iluminación'
    ESCRITORIOS = 'escritorios', 'Escritorios'
    ESTANTERIAS = 'estanterías', 'Estanterías'
    DECORACION = 'decoración', 'Decoración'
    ALFOMBRILLAS = 'alfommbrillas', 'Alfombrillas'
    ORGANIZADORES = 'organizadores', 'Organizadores'
    MISCELANEA = 'miscelánea', 'Miscelánea'

class Foto(models.Model):
    imagen = models.ImageField(upload_to='fotos_producto/')
    producto = models.ForeignKey('Producto', related_name='fotos', on_delete=models.PROTECT)

    def __str__(self):
        return f"Foto de {self.producto.nombre}"
    
    class Meta:
        verbose_name_plural = "Fotos"
        ordering = ['producto']

class Producto(models.Model):
    """Modelo principal para los productos."""
    nombre = models.CharField(max_length=200, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_en_stock = models.PositiveIntegerField(default=0)  # Control de inventario
    categoria = models.TextField(
        choices=Categoria.choices,  # Referencing the choices defined in Status class
        default=Categoria.MISCELANEA
        )
    fabricante = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True, related_name='productos')
    destacado = models.BooleanField(default=False)  # Para escaparate principal
    agotado = models.BooleanField(default=False)  # Para marcar productos sin disponibilidad explícitamente
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name_plural = "Productos"
        ordering = ['nombre']
