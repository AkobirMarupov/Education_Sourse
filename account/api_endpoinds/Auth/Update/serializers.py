from rest_framework import serializers

from account.models import Profile

class ProfileUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'full_name',
            'phone_number',
            'avatar',
            'bio',
            'birth_date',
        )


