from django.contrib import admin
from django import forms

from .models import Center, Teacher, Location, Story, Region, City

class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'phone_number', 'payment_status')
    list_filter = ('payment_status', )
    search_fields = ('name', 'phone_number', 'location')
    list_display_links = ('name', 'owner')


    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.owner == request.user:
            return True
        return False


    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_center_admin


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


admin.site.register(Center, CenterAdmin)



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name','center', 'experience_years', 'bio', 'photo')
    list_display_links = ('full_name', 'center')
    search_fields = ('full_name', 'center__name', 'bio')
    list_filter = ('center', 'experience_years')
    list_filter = ('center',)

admin.site.register(Teacher, TeacherAdmin)



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('region', 'city', 'name', 'center', 'address', 'map_link')
    list_filter = ('center','region', 'city')
    search_fields = ('name', 'region', 'city', 'center__name', 'address')

    @admin.display(description="Google Map")
    def map_link(self, obj):
        if obj.google_map_url:
            return f"<a href='{obj.google_map_url}' target='_blank'>Ko‘rish</a>"
        return "-"
    map_link.allow_tags = True


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'center', 'created_at')
    list_display_links = ('title', 'center')
    list_filter = ('center',)
    search_fields = ('title', 'center__name')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return request.user.is_authenticated and (request.user.is_superuser or request.user.is_center_admin)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_filter = ('region',)
    search_fields = ('name',)
    