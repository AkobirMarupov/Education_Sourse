from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404

from account.api_endpoinds.Auth.List.serializers import ProfileListSerializers
from account.models import Profile

class ProfileListrAPIView(ListAPIView):
    serializer_class = ProfileListSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.all()


class ProfileListOneAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response({'detail': 'Bunday id dagi foydalanuvchi topilmadi.'}, status=404)

