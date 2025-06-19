from rest_framework import serializers
from applications.models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    course_title = serializers.CharField(source='course.title', read_only=True)
    center_name = serializers.CharField(source='center.name', read_only=True)
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = [
            'id', 'student', 'student_name', 'course', 'course_title', 
            'teacher', 'teacher_name', 'center', 'center_name',
            'issue_date', 'certificate_file'
        ]
        read_only_fields = ['certificate_file']

    def get_student_name(self, obj):
        return obj.student.get_full_name()

    def get_teacher_name(self, obj):
        if obj.teacher:
            return obj.teacher.get_full_name()
        return None
