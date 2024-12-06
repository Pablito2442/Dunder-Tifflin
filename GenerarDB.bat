# Ejecutar migraciones para las aplicaciones especificadas
python manage.py makemigrations carrito
python manage.py makemigrations catalogo
python manage.py makemigrations inicio
python manage.py makemigrations login
python manage.py makemigrations pedido
python manage.py makemigrations producto
python manage.py makemigrations usuario

# Aplicar las migraciones
python manage.py migrate

# Ejecutar el seeder
python manage.py seeder

python manage.py collectstatic --noinput
