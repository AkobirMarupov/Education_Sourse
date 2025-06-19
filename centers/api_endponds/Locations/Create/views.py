from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser

from centers.api_endponds.Locations.Create.serializers import LocationCreateSerializer


class LocationCreateAPIView(CreateAPIView):
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Create a new Location",
        request_body=LocationCreateSerializer,
        responses={
            201: openapi.Response(
                description="Location created successfully",
                schema=LocationCreateSerializer
            ),
            400: "Bad Request"
        }
    )    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)    