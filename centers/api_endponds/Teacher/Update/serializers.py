from rest_framework import serializers

from centers.models import Teacher

class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'center',
            'full_name',
            'bio',
            'experience_years',
            'subject',
            'teaching_method',
            'photo'
        ]
        read_only_fields = ['id']
    