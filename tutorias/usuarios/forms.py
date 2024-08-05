from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import Group



class CustomUserCreationFormUsuario(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'gender', 'apellido_materno')  # Asegúrate de ajustar los campos según tu modelo

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationFormUsuario, self).__init__(*args, **kwargs)
        # Aquí puedes añadir cualquier configuración adicional, como personalizar widgets o añadir placeholders
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de Usuario'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo Electrónico'})
        # y así sucesivamente para otros campos