from rest_framework import serializers

from centers.models import Center


class CenterUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = [
            'id',
            'name',
            'description',
            'location',
            'image',
            'phone_number',
            'payment_status',
            ]
        read_only_fields = ['id']
        