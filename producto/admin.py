from django.contrib import admin
from .models import Producto, Categoria, Fabricante

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'fabricante', 'destacado', 'agotado')
    list_filter = ('categoria', 'fabricante', 'destacado', 'agotado')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('precio', 'stock', 'destacado', 'agotado')
