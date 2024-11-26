from django.contrib import admin
from .models import *


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'email', 'numTlf', 'web', 'pais')
    search_fields = ('nombre', 'descripcion', 'email', 'numTlf', 'web', 'pais')
    list_filter = ('pais',)
    list_editable = ('email', 'numTlf', 'web', 'pais')
    list_display_links = ('nombre',)

@admin.register(Foto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto',)
    list_display_links = ('producto',)
    search_fields = ('producto__name',)
    list_filter = ('producto',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'cantidadEnStock', 'categoria', 'fabricante', 'destacado', 'agotado')
    list_filter = ('categoria', 'fabricante', 'destacado', 'agotado')
    search_fields = ('nombre', 'descripcion', 'fecha_creacion', 'fecha_actualizacion')
    list_editable = ('precio', 'cantidadEnStock', 'categoria', 'fabricante', 'destacado')
    list_display_links = ('nombre',)
