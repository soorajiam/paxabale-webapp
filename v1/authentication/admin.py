from django.contrib import admin
from .models import CustomUser
# Register your models here.
# use admin view to manage users
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('bio',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

    
