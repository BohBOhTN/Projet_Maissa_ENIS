# users/admin.py
from django.contrib import admin
from .models import User, AdminUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email')

class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_super_admin')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')


admin.site.register(User)
admin.site.register(AdminUser)
