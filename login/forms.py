from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario / Correo Electronico', 'class': 'login__input'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'login__input'}))

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su Nombre', 'class': 'nombres__input'}),
        label='Nombre'
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su Apellido', 'class':'apellidos__input'}),
        label='Apellido'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su Correo', 'class': 'correo'}),
        label='Correo electrónico'
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su Usuario', 'class': 'usuario'}),
        label='Nombre de usuario'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su Contraseña', 'class': 'password'}),
        label='Contraseña'
    )