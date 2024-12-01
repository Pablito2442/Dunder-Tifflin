from django.core.management.base import BaseCommand
from datetime import date, datetime as dt
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
                            precio=200, cantidad_en_stock=10, categoria = Categorias.sillas,
                            fabricante= Fabricantes.pepe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-25'),fecha_actualizacion= date('2024-11-27'),
                            foto= "images/silla_gamer.jpg")
    
    Producto.objects.create(nombre="Lámpara de cristal", descripcion="Lámpara muy elegante hecha parcialmente de vidreo",
                            precio=140, cantidad_en_stock=10, categoria = Categorias.iluminacion,
                            fabricante= Fabricantes.pierre, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-23') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/lampara_de_cristal.jpg")
    
    Producto.objects.create(nombre="Sillón gris", descripcion="Sillón perfecto para cualquier salón",
                            precio=40, cantidad_en_stock=10, categoria = Categorias.sillas,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/sillon_gris.jpg")
    
    Producto.objects.create(nombre="Escritorio de hierro", descripcion="Escritorio de hierro forjado, muy resistente",
                            precio=350, cantidad_en_stock=10, categoria = Categorias.escritorios,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/escritorio 1.jpg")
    
    Producto.objects.create(nombre="Escritorio madera", descripcion="Escritorio de madera maciza, muy resistente",
                            precio=150, cantidad_en_stock=10, categoria = Categorias.escritorios,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/escritorio 2.jpg")
    
    Producto.objects.create(nombre="Escritorio moderno", descripcion="Escriotrio de madera y metal, muy moderno y práctico",
                            precio=180, cantidad_en_stock=10, categoria = Categorias.escritorios,
                            fabricante= Fabricantes.pepe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/escritorio 3.jpg")
    
    Producto.objects.create(nombre="Escritorio simple", descripcion="Escriotrio de madera pequeño y sencillo",
                            precio=60, cantidad_en_stock=10, categoria = Categorias.escritorios,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/escritorio 4.jpg")
    
    Producto.objects.create(nombre="Escritorio en L", descripcion="Escriotrio de madera en forma de L, muy práctico y grande",
                            precio=200, cantidad_en_stock=10, categoria = Categorias.escritorios,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/escritorio 5.jpg")
    
    Producto.objects.create(nombre="Escritorio señorial", descripcion="Escriotrio de madera maciza en forma de L, muy elegante y grande",
                            precio=600, cantidad_en_stock=4, categoria = Categorias.escritorios,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/escritorio 6.jpg")
    
    Producto.objects.create(nombre="Estante blanco", descripcion="Estantería de madera y color blanco, muy elegante",
                            precio=60, cantidad_en_stock=20, categoria = Categorias.estanterias,
                            fabricante= Fabricantes.pepe, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/estante 1.jpg")
    
    Producto.objects.create(nombre="Estante blanco abierto", descripcion="Estante abierto de madera y color blanco, muy elegante",
                            precio=50, cantidad_en_stock=20, categoria = Categorias.estanterias,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/estante 2.jpg")
    
    Producto.objects.create(nombre="Estante simple abierto", descripcion="Estante abierto de acero y color blanco, muy práctico",
                            precio=20, cantidad_en_stock=20, categoria = Categorias.estanterias,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/estante 3.jpg")
    
    Producto.objects.create(nombre="Estante madera clásico", descripcion="Estante de madera clásico, practico y elegante",
                            precio=60, cantidad_en_stock=20, categoria = Categorias.estanterias,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/estante 4.jpg")
    
    Producto.objects.create(nombre="Estante hierro moderno", descripcion="Estante de hierro moderno, muy resistente",
                            precio=70, cantidad_en_stock=20, categoria = Categorias.estanterias,
                            fabricante= Fabricantes.pepe, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/estante 5.jpg")
    
    Producto.objects.create(nombre="Silla confort", descripcion="Silla de oficina muy cómoda, sin reposacabezas",  
                            precio=80, cantidad_en_stock=20, categoria = Categorias.sillas,
                            fabricante= Fabricantes.pepe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/silla 1.jpg")
    
    Producto.objects.create(nombre="Silla reposacabeza", descripcion="Silla de oficina muy cómoda, con reposacabezas",  
                            precio=100, cantidad_en_stock=20, categoria = Categorias.sillas,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/silla 2.jpg")

    Producto.objects.create(nombre="Silla beige", descripcion="Silla de oficina muy cómoda, sin reposacabezas",  
                            precio=90, cantidad_en_stock=20, categoria = Categorias.sillas,
                            fabricante= Fabricantes.pepe, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/silla 3.jpg")
    
    Producto.objects.create(nombre="Silla simple negra", descripcion="Silla de oficina cómoda, sin reposacabezas",  
                            precio=60, cantidad_en_stock=20, categoria = Categorias.sillas,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24') ,fecha_actualizacion= date('2024-11-27'),
                            foto="images/silla 4.jpg")
    
    Producto.objects.create(nombre="Organizador de escritorio", descripcion="Organizador de escritorio de tela",
                            precio=10, cantidad_en_stock=15, categoria = Categorias.organizadores,
                            fabricante= Fabricantes.pepe, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/organizador 6.jpg")

    Producto.objects.create(nombre="Organizador con cajones XL", descripcion="Organizador de escritorio con cajones de plástico grande",
                            precio=20, cantidad_en_stock=25, categoria = Categorias.organizadores,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/organizador 2.jpg")

    Producto.objects.create(nombre="Organizador con cajones", descripcion="Organizador de escritorio con cajones de plástico",
                            precio=15, cantidad_en_stock=20, categoria = Categorias.organizadores,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/organizador 3.jpg")

    Producto.objects.create(nombre="Organizador de escritorio grande", descripcion="Organizador de escritorio grande de plástico",
                            precio=35, cantidad_en_stock=10, categoria = Categorias.organizadores,
                            fabricante= Fabricantes.pepe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/organizador 4.jpg")

    Producto.objects.create(nombre="Organizador invisible", descripcion="Organizados de escritorio transparente",
                            precio=10, cantidad_en_stock=5, categoria = Categorias.organizadores,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/organizador 5.jpg")

    Producto.objects.create(nombre="Organizador de cocina", descripcion="Organizador para productos de cafe",
                            precio=10, cantidad_en_stock=8, categoria = Categorias.organizadores,
                            fabricante= Fabricantes.pierre, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/organizador 1.jpg")
    
    Producto.objects.create(nombre="Alfombrilla ergonómica", descripcion="Alfombrilla ergonómica para ratón",  
                            precio=15, cantidad_en_stock=30, categoria = Categorias.alfombrillas,
                            fabricante= Fabricantes.pepe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/alfombrilla 1.jpg")

    Producto.objects.create(nombre="Alfombrilla rosa", descripcion="Alfombrilla simple de tela rosa",  
                            precio=10, cantidad_en_stock=20, categoria = Categorias.alfombrillas,
                            fabricante= Fabricantes.joe, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/alfombrilla 2.jpg")

    Producto.objects.create(nombre="Alfombrilla mapamundi Xl", descripcion="Alfombrilla de tela con mapamundi",  
                            precio=20, cantidad_en_stock=50, categoria = Categorias.alfombrillas,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/alfombrilla 3.jpg")
    
    Producto.objects.create(nombre="Rueda recambio metal", descripcion="Rueda de recambio para silla de oficina",  
                            precio=15, cantidad_en_stock=50, categoria = Categorias.miscelanea,
                            fabricante= Fabricantes.pierre, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/miscelanea 1.jpg")
    
    Producto.objects.create(nombre="Calendario 2025", descripcion="Calendario de escritorio 2025",  
                            precio=7, cantidad_en_stock=50, categoria = Categorias.miscelanea,
                            fabricante= Fabricantes.pepe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/miscelanea 2.jpg")
    
    Producto.objects.create(nombre="Reloj de pared", descripcion="Reloj de pared de plastico moderno",  
                            precio=15, cantidad_en_stock=30, categoria = Categorias.miscelanea,
                            fabricante= Fabricantes.joe, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/miscelanea 3.jpg")
    
    Producto.objects.create(nombre="Rueda recambio", descripcion="Rueda de recambio para silla de oficina",  
                            precio=10, cantidad_en_stock=50, categoria = Categorias.miscelanea,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/miscelanea 4.jpg")
    
    Producto.objects.create(nombre="Bombilla inteligente", descripcion="Bombilla inteligente para controlar con el móvil",  
                            precio=15, cantidad_en_stock=15, categoria = Categorias.iluminacion,
                            fabricante= Fabricantes.pierre, destacado=True, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/luz 2.jpg")
    
    Producto.objects.create(nombre="Lampara madera", descripcion="Lampara de madera, muy bonita",  
                            precio=35, cantidad_en_stock=15, categoria = Categorias.iluminacion,
                            fabricante= Fabricantes.pierre, destacado=False, agotado=False,
                            fecha_creacion= date('2024-11-24'), fecha_actualizacion= date('2024-11-27'),
                            foto="images/luz 1.jpg")
    
def date(string):
    return dt.strptime(string, '%Y-%m-%d')