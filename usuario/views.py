from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

#
# Vistas y Botones de la vista de index
#

def panel_informacion_general(request):
    user = request.user
    
    return render(request, 'index.html', {'user': user})

def modificar_informacion_usuario(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        usuario_id = request.POST.get('usuario_id')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Buscar el usuario en la base de datos
        user = User.objects.get(id=usuario_id)

        # Actualizar los campos del usuario
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        # Mostrar un mensaje de éxito
        messages.success(request, 'La información se actualizó correctamente.')

        return redirect('panel_usuario')  # Redirige al panel de usuario después de actualizar

    return redirect('panel_usuario') 

def cambiar_contraseña(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        usuario_id = request.user.id  # El ID del usuario actual
        current_password = request.POST.get('current_password')  # Contraseña actual
        new_password = request.POST.get('new_password')  # Nueva contraseña
        confirm_new_password = request.POST.get('confirm_new_password')  # Confirmación de nueva contraseña

        # Buscar el usuario en la base de datos
        user = User.objects.get(id=usuario_id)

        # Verificar si la contraseña actual es correcta
        if not check_password(current_password, user.password):
            messages.error(request, 'La contraseña actual es incorrecta.')
            return redirect('panel_usuario')  # Redirige a la página de información del usuario

        # Verificar si las contraseñas nuevas coinciden
        if new_password != confirm_new_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('panel_usuario')  # Redirige a la página de información del usuario

        # Cambiar la contraseña
        user.set_password(new_password)  # Establecer la nueva contraseña
        user.save()  # Guardar el usuario con la nueva contraseña

        # Mantener la sesión activa después de cambiar la contraseña
        update_session_auth_hash(request, user)

        # Mostrar un mensaje de éxito
        messages.success(request, 'La contraseña se cambió correctamente.')

        return redirect('panel_usuario')  # Redirige a la página de información del usuario

    return redirect('panel_usuario')  # Si no es un POST, redirige al panel de usuario


#
# Vistas y Botones de la vista de pedidos
#

def panel_pedidos(request):
    return render(request, 'pedidos.html')


#
# Vistas y Botones de la vista de pagos
#

def panel_pagos(request):
    return render(request, 'pagos.html')


#
# Vistas y Botones de la vista de administracion productos
#

def panel_tablas_productos_administracion(request):
    return render(request, 'administracion_productos.html')


#
# Vistas y Botones de la vista de administracion Usuarios
#

def panel_tablas_usuarios_administracion(request):   
    usuarios = User.objects.all()
    
    return render(request, 'administracion_usuarios.html', {'usuarios': usuarios})

def modificar_usuario_administrados(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        try:
            user = User.objects.get(id=usuario_id)
            
            # Actualizar campos básicos
            user.first_name = request.POST.get('first_name', '').strip()
            user.last_name = request.POST.get('last_name', '').strip()
            user.email = request.POST.get('email', '').strip()

            # Manejar el checkbox is_staff
            is_staff_value = request.POST.get('is_staff')
            user.is_staff = True if is_staff_value == 'on' else False

            user.save()
            return JsonResponse({'success': True})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Usuario no encontrado'})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

def eliminar_usuario(request, usuario_id):
    if request.method == 'POST':
        usuario = get_object_or_404(User, id=usuario_id)
        usuario.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'})


#
# Vistas y Botones de la vista de administracion pedidos
#

def panel_tablas_pedidos_administracion(request):
    return render(request, 'administracion_pedidos.html')


#
# Vistas y Botones de la vista de administracion pagos
#

def panel_tablas_pagos_administracion(request):
    return render(request, 'administracion_pagos.html')