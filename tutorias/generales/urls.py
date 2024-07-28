from django.urls import path
from .views import CustomLoginView, home

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('', CustomLoginView.as_view()),  # Redirigir al login por defecto
]
