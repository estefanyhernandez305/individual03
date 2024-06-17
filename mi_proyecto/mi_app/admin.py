from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefono', 'direccion', 'fecha_nacimiento')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)