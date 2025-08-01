from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser
from centers.permissions import IsCenterAdmin

from centers.api_endponds.Teacher.Create.serializers import TeacherCreateSerializer
from centers.models import Teacher


class TeacherCreateAPIView(CreateAPIView):
    serializer_class = TeacherCreateSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated, IsCenterAdmin]

    @swagger_auto_schema(
        operation_description="Yangi o'qituvchi qo'shish",
        manual_parameters=[
            openapi.Parameter('center', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('center', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('full_name', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('bio', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('experience_years', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('subject', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter(
                'teaching_method',
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                required=True,
                enum=[choice[0] for choice in Teacher.PAYMENT_STATUS_CHOICES],
                enum_names=[choice[1] for choice in Teacher.PAYMENT_STATUS_CHOICES],
            ),
            openapi.Parameter('photo', openapi.IN_FORM, type=openapi.TYPE_FILE, required=False)
        ],
        responses={201: TeacherCreateSerializer}
    )

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        serializer.save()
