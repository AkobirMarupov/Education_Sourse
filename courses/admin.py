from django.contrib import admin

from courses.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('center', 'title', 'description', 'duration', 'price', 'language', 'schedule')
    list_display_links = ('center', 'title', 'description')
    search_fields = ('center__name', 'price')
    list_filter = ('center',)

admin.site.register(Course, CourseAdmin)