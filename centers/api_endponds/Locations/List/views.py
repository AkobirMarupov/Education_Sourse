from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from centers.permissions import IsCenterAdmin

from centers.models import Location
from centers.api_endponds.Locations.List.serializers import LocationListSerializer


class LocationsListAPIView(ListAPIView):
    serializer_class = LocationListSerializer
    permission_classes = [IsAuthenticated, IsCenterAdmin]
    
    def get_queryset(self):
        return Location.objects.all()
    
class LocationDetailAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer
    permission_classes = [IsAuthenticated, IsCenterAdmin]
    lookup_field = 'id'

    def get_object(self):
        course_id = self.kwargs.get('id')
        try:
            return Location.objects.get(id=course_id)
        except Location.DoesNotExist:
            raise NotFound(detail="Bunday ID dagi joy topilmadi", code=404)