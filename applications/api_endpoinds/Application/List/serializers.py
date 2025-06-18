from rest_framework import serializers

from applications.models import Application


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            'student',
            'center',
            'course',
            'teacher',
            'first_name',
            'last_name',
            'phone_number',
            'birth_date',
            'status',
        ]