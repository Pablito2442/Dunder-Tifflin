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
class FotoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'imagen')
    list_display_links = ('producto',)
    search_fields = ('producto',)
    list_filter = ('producto',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'cantidad_en_stock', 'categoria', 'fabricante', 'destacado', 'agotado')
    list_filter = ('categoria', 'fabricante', 'destacado', 'agotado')
    search_fields = ('nombre', 'descripcion', 'fecha_creacion', 'fecha_actualizacion')
    list_editable = ('precio', 'cantidad_en_stock', 'categoria', 'fabricante', 'destacado')
    list_display_links = ('nombre',)
