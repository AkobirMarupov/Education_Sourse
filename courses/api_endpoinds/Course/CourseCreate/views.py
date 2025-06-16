from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from centers.models import Course
from courses.api_endpoinds.Course.CourseCreate.serializers import CourseCreateSerializer


class CourseCreateAPIView(GenericAPIView):
    serializer_class = CourseCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

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
        responses={201: CourseCreateSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
