from rest_framework import serializers

from centers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'full_name',
            'bio',
            'experience_years',
            'subject',
            'teaching_method',
            'photo'
        ]