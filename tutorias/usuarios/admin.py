from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('gender',)}),
    )
    list_display = UserAdmin.list_display + ('gender_display',)

    def gender_display(self, obj):
        return obj.get_gender_display()
    gender_display.short_description = 'Género'

admin.site.register(CustomUser, CustomUserAdmin)