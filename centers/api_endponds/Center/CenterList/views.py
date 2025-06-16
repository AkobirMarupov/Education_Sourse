from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from centers.models import Center
from centers.api_endponds.Center.CenterList.serializers import CenterListSerializer


class CenterListAPIView(ListAPIView):
    serializer_class = CenterListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Center.objects.all()
    

class CenterDetailAPIView(RetrieveAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

