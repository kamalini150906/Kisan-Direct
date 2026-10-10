from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Marketplace Info', {'fields': ('role', 'phone', 'village', 'district')}),)
    list_display = ('username', 'role', 'phone', 'village', 'is_staff')
    list_filter = ('role', 'district')

admin.site.register(User, CustomUserAdmin)
