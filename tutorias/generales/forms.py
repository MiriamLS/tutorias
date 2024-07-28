from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario o Correo Electrónico',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario o Correo Electrónico'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError("Esta cuenta está desactivada.", code='inactive')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Intenta autenticar primero por nombre de usuario
            user = authenticate(self.request, username=username, password=password)
            if user is None:
                # Si falla, intenta buscar el usuario por email y autenticar por nombre de usuario
                try:
                    user_temp = User.objects.get(email=username)
                    user = authenticate(self.request, username=user_temp.username, password=password)
                except User.DoesNotExist:
                    pass

            if user is None:
                raise forms.ValidationError('Usuario o contraseña incorrecta. Por favor, inténtalo de nuevo.', code='invalid_login')

        # Asigna el usuario al atributo del formulario para su uso posterior
        self.user_cache = user
        return self.cleaned_data
