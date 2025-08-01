from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from centers.permissions import IsCenterAdmin

from centers.api_endponds.Teacher.List.serializers import TeacherSerializer
from centers.models import Teacher


class TeasherListAPIView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsCenterAdmin]
    
    def get_queryset(self):
        return Teacher.objects.all()
    
class TeacherRetriAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_object(self):
        course_id = self.kwargs.get('id')
        try:
            return Teacher.objects.get(id=course_id)
        except Teacher.DoesNotExist:
            raise NotFound(detail="Bunday ID dagi O`qituvchi topilmadi", code=404)