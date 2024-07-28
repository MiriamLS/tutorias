from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'apellido_materno', 'email', 'gender')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'apellido_materno', 'email', 'gender', 'is_staff', 'is_active', 'groups'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'apellido_materno', 'gender_display', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'gender')

    def gender_display(self, obj):
        return obj.get_gender_display()
    gender_display.short_description = 'Género'


admin.site.register(CustomUser, CustomUserAdmin)