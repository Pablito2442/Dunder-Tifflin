from django.db import models

class Categoria(models.Model):
    """Representa la categoría a la que pertenece un producto."""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ['nombre']


class Fabricante(models.Model):
    """Representa el fabricante o la marca del producto."""
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fabricantes"
        ordering = ['nombre']


class Producto(models.Model):
    """Modelo principal para los productos."""
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Control de inventario
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True, related_name='productos')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Imagen única por producto
    destacado = models.BooleanField(default=False)  # Para escaparate principal
    agotado = models.BooleanField(default=False)  # Para marcar productos sin disponibilidad explícitamente
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def en_stock(self):
        """Devuelve True si el producto está disponible."""
        return self.stock > 0 and not self.agotado

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ['nombre']
