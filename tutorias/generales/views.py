from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomAuthenticationForm
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrecta. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def home(request):
    return render(request, 'home.html')