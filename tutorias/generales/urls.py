from django.urls import path
from .views import CustomLoginView, exit_view, home

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('', CustomLoginView.as_view()),  # Redirigir al login por defecto
    path('exit/', exit_view, name='exit'),  # Ruta para cerrar sesión
    

]
