from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404

from applications.api_endpoinds.Application.List.serializers import ApplicationListSerializer
from applications.models import Application


class ApplicationListAPIView(ListAPIView):
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.all()


class ApplicationRetrievAPIView(RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response({"detail": "Bu ID dagi ariza topilmadi."}, status=404)
