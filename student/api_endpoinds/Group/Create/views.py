from rest_framework import generics, permissions
from student.models import StudentGroup
from .serializers import (
    StudentGroupCreateSerializer,
    StudentGroupListSerializer
)
from student.permissions import IsCenterAdmin
from rest_framework.exceptions import ValidationError


class StudentGroupCreateAPIView(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsCenterAdmin]

    def perform_create(self, serializer):
        user = serializer.validated_data['user']
        group = serializer.validated_data['group']
        if StudentGroup.objects.filter(user=user, group=group).exists():
            raise ValidationError("Ushbu foydalanuvchi bu guruhga allaqachon qo‘shilgan.")
        serializer.save()



class MyGroupsAPIView(generics.ListAPIView):
    serializer_class = StudentGroupListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudentGroup.objects.filter(user=self.request.user).select_related('group__teacher', 'group__course', 'group__center').prefetch_related('group__days')
