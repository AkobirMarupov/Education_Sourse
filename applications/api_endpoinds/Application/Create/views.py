from rest_framework.generics import CreateAPIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from applications.models import Application
from applications.api_endpoinds.Application.Create.serializers import ApplicationSerializer


class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create a new application",
        request_body=ApplicationSerializer, 
        responses={201: ApplicationSerializer}
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
