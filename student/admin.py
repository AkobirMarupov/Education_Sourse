from django.contrib import admin
from .models import Group, StudentGroup, GroupDayTime

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'center', 'course', 'teacher', 'start_date')
    list_filter = ('center', 'course', 'start_date')
    search_fields = ('name', 'teacher__full_name')


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'joined_at')
    list_filter = ('group__center', 'joined_at')
    search_fields = ('user__username', 'group__name')


@admin.register(GroupDayTime)
class GroupDayTimeAdmin(admin.ModelAdmin):
    list_display = ('weekday', 'time')