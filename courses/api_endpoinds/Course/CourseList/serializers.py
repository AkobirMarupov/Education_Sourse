from rest_framework import serializers

from centers.models import Course

class CourseListSerializer(serializers.ModelSerializer):
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
        read_only_fields = ('id', )