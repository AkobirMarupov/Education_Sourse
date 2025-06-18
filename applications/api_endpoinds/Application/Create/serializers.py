from rest_framework import serializers

from applications.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
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
        read_only_fields = ['id', 'student']

    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user 
        return super().create(validated_data)

