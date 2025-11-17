from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ("Informações adicionais", {'fields': ('nome', 'telefone', 'cpf')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'telefone', 'cpf', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    list_display = ('email', 'nome', 'telefone', 'cpf', 'is_active', 'is_staff')
    search_fields = ('email', 'nome', 'telefone')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
