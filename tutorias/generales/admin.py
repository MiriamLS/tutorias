from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Posgrado

@admin.register(Posgrado)
class PosgradoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
    list_filter = ('fecha_creacion', 'fecha_actualizacion')