from rest_framework import serializers
from student.models import StudentGroup, Group


class GroupDayTimeSerializer(serializers.ModelSerializer):
    weekday_display = serializers.CharField(source='get_weekday_display', read_only=True)

    class Meta:
        model = Group.days.rel.model
        fields = ['weekday', 'weekday_display', 'time']


class GroupSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    center = serializers.StringRelatedField()
    days = GroupDayTimeSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'course', 'teacher', 'center', 'start_date', 'days']


class StudentGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['user', 'group']


class StudentGroupListSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = StudentGroup
        fields = ['group', 'joined_at']
