from django.core.management.base import BaseCommand
from datetime import datetime as dt
from producto.models import *

# Para usar el seeder, ejecutad: python manage.py seeder
class Command(BaseCommand):
    def handle(self, *args, **options):
        vaciar()
        seed()

def vaciar():
    Categoria.objects.all().delete()
    Fabricante.objects.all().delete()
    Producto.objects.all().delete()

def seed():
    #Las entidades creadas están separados en clases por organización
    class Categorias:
        sillas =        Categoria.objects.create(nombre="Sillas", slug="sillas")
        iluminacion =   Categoria.objects.create(nombre="Iluminación", slug="iluminacion")
        escritorios =   Categoria.objects.create(nombre="Escritorios", slug="escritorios")
        estanterias =   Categoria.objects.create(nombre="Estanterías", slug="estanterias")
        decoracion =    Categoria.objects.create(nombre="Decoración", slug="decoracion")
        alfombrillas =  Categoria.objects.create(nombre="Alfombrillas", slug="alfombrillas")
        organizadores = Categoria.objects.create(nombre="Organizadores", slug="organizadores")
        miscelanea =    Categoria.objects.create(nombre="Miscelánea", slug="miscelanea")

    class Fabricantes:
        pepe =  Fabricante.objects.create(nombre="Pepe Fabrica", descripcion="Mi pasión son los muebles", 
                                email="pepe@pepefabrica.es", numTlf="612047393",
                                web="https://www.pepefabrica.es", pais=Country.SPAIN)
        joe =   Fabricante.objects.create(nombre="Joe's furniture", descripcion="Real American Furniture",
                                email="contactme@joesfurniture.com", numTlf="56428383",
                                web="https://joesfurniture.com", pais=Country.USA)
        pierre =Fabricante.objects.create(nombre="Meubles Jean Pierre", descripcion="Autenticos muebles parisinos de alta calidad",
                                email="contactez-nous@jpierremeubles.fr", numTlf="864158735",
                                web="https://jpierremeubles.fr", pais=Country.FRANCE) # Meubles no está mal escrito, es muebles en francés

    Producto.objects.create(nombre="Silla gamer", descripcion="Silla hecha para pasar varias horas jugando a videojuegos",
                            precio=200, cantidad_en_stock=500, categoria = Categorias.sillas,
                            fabricante= Fabricantes.pepe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-25'),fecha_actualizacion= date('2024-11-27'),
                            foto="silla_gamer.jpg")
    Producto.objects.create(nombre="Lámpara de cristal", descripcion="Lámpara muy elegante hecha parcialmente de vidreo",
                            precio=140, cantidad_en_stock=200, categoria = Categorias.iluminacion,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-23') ,fecha_actualizacion= date('2024-11-27'),
                            foto="lampara_de_cristal.jpg")
    Producto.objects.create(nombre="Sillón gris", descripcion="Sillón perfecto para cualquier salón",
                            precio=1, cantidad_en_stock=2000, categoria = Categorias.sillas,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="sillon_gris.jpg")

def date(string):
    return dt.strptime(string, '%Y-%m-%d')