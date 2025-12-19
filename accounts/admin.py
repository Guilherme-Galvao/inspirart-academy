from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_instructor', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_instructor', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_instructor', 'bio')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
