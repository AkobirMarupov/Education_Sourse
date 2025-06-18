from django.contrib import admin

from courses.models import Course , CourseResource

class CourseAdmin(admin.ModelAdmin):
    list_display = ('center', 'title', 'description', 'duration', 'price', 'language', 'schedule')
    list_display_links = ('center', 'title', 'description')
    search_fields = ('center__name', 'price')
    list_filter = ('center',)

admin.site.register(Course, CourseAdmin)


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'link']
    search_fields = ['title', 'course__title']