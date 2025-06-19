from django.contrib import admin

from .utils.certificate_generator import generate_certificate_pdf
from .models import Application, Certificate

@admin.register(Application)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['student', 'center', 'teacher', 'first_name', 'last_name', 'phone_number', 'birth_date', 'status']
    list_display_links = ['student', 'center', 'teacher', 'first_name', 'last_name']
    list_filter = ['student', 'center', 'teacher', 'first_name', 'last_name', 'phone_number']
    search_fields = ['student', 'teacher', 'first_name', 'last_name', 'phone_number', 'birth_date', 'status']




@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'center', 'issue_date')
    actions = ['generate_pdf']

    def generate_pdf(self, request, queryset):
        for certificate in queryset:
            generate_certificate_pdf(certificate)
        self.message_user(request, "PDF sertifikatlar yaratildi!")

    generate_pdf.short_description = "Tanlangan sertifikatlar uchun PDF yaratish"