from django.contrib import admin

from .models import Application

@admin.register(Application)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['student', 'center', 'teacher', 'first_name', 'last_name', 'phone_number', 'birth_date', 'status']
    list_display_links = ['student', 'center', 'teacher', 'first_name', 'last_name']
    list_filter = ['student', 'center', 'teacher', 'first_name', 'last_name', 'phone_number']
    search_fields = ['student', 'teacher', 'first_name', 'last_name', 'phone_number', 'birth_date', 'status']