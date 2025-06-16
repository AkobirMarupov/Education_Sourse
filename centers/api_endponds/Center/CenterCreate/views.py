from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from centers.models import Center
from centers.api_endponds.Center.CenterCreate.serializers import CenterCreateSerializer


class CenterCreateAPIView(GenericAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterCreateSerializer
    parser_classes = [MultiPartParser, FormParser]  
    permission_classes = [IsAuthenticated]  

    @swagger_auto_schema(
        operation_description="Create new center",
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('description', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('location', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('image', openapi.IN_FORM, type=openapi.TYPE_FILE, required=True),
            openapi.Parameter('phone_number', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('payment_status', openapi.IN_FORM, type=openapi.TYPE_STRING, enum=['free', 'premium', 'gold'], required=True),
        ],
        responses={201: CenterCreateSerializer}
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
