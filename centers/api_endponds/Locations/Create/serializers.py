from rest_framework import serializers

from centers.models import Location

class LocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'center',
            'name',
            'address',
            'latitude',
            'longitude',
        )