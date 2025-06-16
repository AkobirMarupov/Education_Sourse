from rest_framework import serializers

from centers.models import Location


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id',
            'center',
            'name',
            'address',
            'latitude',
            'longitude',
        ]