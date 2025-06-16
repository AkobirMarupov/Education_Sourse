from rest_framework import serializers

from centers.models import Course


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = (
            'id',
            'center',
            'title',
            'description',
            'price',
            'language',
            'duration',
            'schedule'
        )