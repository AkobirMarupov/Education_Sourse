from rest_framework import serializers

from centers.models import Center

class CenterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = [
            'id',
            'name',
            'owner',
            'location',
            'image',
            'phone_number',
        ]
        read_only_fields = ('id', )
    