from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from centers.models import Center
from centers.api_endponds.Center.CenterUpdate.serializers import CenterUpdateSerializer


class CenterUpdateAPIView(GenericAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    lookup_field = 'id'


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