from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from centers.models import Course
from courses.api_endpoinds.Course.CourseUpdate.serializers import CourseUpdateSerializer


class CourseUpdateAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_description="Create a new course",
        manual_parameters=[
            openapi.Parameter('center', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('title', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('description', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('price', openapi.IN_FORM, type=openapi.TYPE_NUMBER, required=True),
            openapi.Parameter('language', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),

            openapi.Parameter(
                'duration',
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                required=True,
                enum=[choice[0] for choice in Course.PAYMENT_STATUS_CHOICES],
                enum_names=[choice[1] for choice in Course.PAYMENT_STATUS_CHOICES],
                description="Kurs davomiyligi"
            ),
            openapi.Parameter(
                'schedule',
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                required=True,
                enum=[choice[0] for choice in Course.PAYMENT_STATUS_DATE],
                enum_names=[choice[1] for choice in Course.PAYMENT_STATUS_DATE],
                description="Dars jadvali"
            ),
        ],
        responses={201: CourseUpdateSerializer},
    )
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save()
    

    