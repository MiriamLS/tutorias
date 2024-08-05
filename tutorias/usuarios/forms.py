from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from generales.models import Posgrado
from .models import CustomUser
from django.contrib.auth.models import Group



class CustomUserCreationFormUsuario(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Ordena los campos según deseas que aparezcan en el formulario
        fields = ('username','first_name', 'last_name', 'apellido_materno', 'email', 'password1', 'password2', 'gender', 'posgrado')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationFormUsuario, self).__init__(*args, **kwargs)

        # Configuración del campo 'username' para usar 'Número de Control' como placeholder y label
        self.fields['username'].widget.attrs.update({'placeholder': 'Número de Control'})
        self.fields['username'].label = 'Número de Control'

        # Configuración de placeholders para otros campos
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombre'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido Paterno'})
        self.fields['apellido_materno'].widget.attrs.update({'placeholder': 'Apellido Materno'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo Electrónico'})

        # Hacer que los campos sean requeridos según sea necesario
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['apellido_materno'].required = True

        # Campos adicionales
        self.fields['gender'].required = False  # Si el género es opcional
        self.fields['posgrado'].queryset = Posgrado.objects.all()
        self.fields['posgrado'].label = 'Posgrado'
        self.fields['posgrado'].required = True
