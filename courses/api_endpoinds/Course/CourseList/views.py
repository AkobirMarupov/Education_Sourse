from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from centers.models import Course
from courses.api_endpoinds.Course.CourseList.serializers import CourseListSerializer


class CourseListAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Course.objects.all()
    
    
class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        course_id = self.kwargs.get('id')
        try:
            return Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise NotFound(detail="Bunday ID dagi kurs topilmadi", code=404)