from django.urls import path
from .views import CoordinadoresListView, DocentesListView, AlumnosListView

urlpatterns = [
    path('coordinadores/', CoordinadoresListView.as_view(), name='coordinadores-list'),
    path('docentes/', DocentesListView.as_view(), name='docentes-list'),
    path('alumnos/', AlumnosListView.as_view(), name='alumnos-list'),
]