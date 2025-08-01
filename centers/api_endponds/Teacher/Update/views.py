from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from centers.permissions import IsCenterAdmin
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from centers.models import Teacher
from centers.api_endponds.Teacher.Update.serializers import TeacherUpdateSerializer
from centers.models import Teacher


class TeacherUpdateView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherUpdateSerializer
    permission_classes = [IsAuthenticated, IsCenterAdmin]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'id'

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
        responses={201: TeacherUpdateSerializer}
    )

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

