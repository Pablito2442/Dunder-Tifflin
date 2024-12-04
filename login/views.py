from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
import re

def user_login(request):
    next_url = request.GET.get('next', 'inicio')  # Obtener la URL de redirección
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # Comprobar si el valor ingresado es un correo electrónico
            username_or_email = cd['username']
            user = None

            # Si es un correo electrónico, buscar el usuario por correo
            if re.match(r"[^@]+@[^@]+\.[^@]+", username_or_email):
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    messages.error(request, 'Ingreso inválido')
                    return redirect('login')  # Redirigir para mostrar el mensaje de error
            else:
                # Si no es un correo, buscar por el nombre de usuario
                user = User.objects.filter(username=username_or_email).first()

            # Intentar la autenticación con el usuario encontrado
            if user:
                user = authenticate(request, username=user.username, password=cd['password'])

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(next_url)  # Redirigir a la URL anterior
                    else:
                        messages.error(request, 'Cuenta deshabilitada')
                        return redirect('login')
                else:
                    messages.error(request, 'Ingreso inválido')
                    return redirect('login')
            else:
                messages.error(request, 'Ingreso inválido')
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'next': next_url})

def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Crear el usuario
            try:
                # Verificar si ya existe un usuario con el mismo nombre de usuario o correo
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'El nombre de usuario ya está en uso.')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'El correo electrónico ya está registrado.')
                else:
                    # Crear el usuario
                    user = User.objects.create(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=make_password(password)  # Encriptar la contraseña antes de guardarla
                    )
                    messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
                    return redirect('login')  # Redirigir a la página de login con el mensaje de éxito
            except Exception as e:
                messages.error(request, f'Error al crear el usuario: {str(e)}')
    else:
        form = RegisterForm()

    # Personalizar la clase 'login__input' en cada campo
    for field in form:
        field.field.widget.attrs.update({'class': 'login__input'})

    return render(request, 'registro.html', {'form': form})
