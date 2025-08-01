# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'is_active', 'is_staff', 'is_confirmed', 'is_center_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Other info', {'fields': ('is_confirmed',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_center_admin')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'full_name', 'phone_number', 'bio', 'birth_date')
    search_fields = ('user__email', 'full_name')
    list_filter = ('birth_date',)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.user == request.user:
            return True
        return False
    