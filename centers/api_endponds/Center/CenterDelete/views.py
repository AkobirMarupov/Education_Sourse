from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from centers.models import Center


class CenterDeleteAPIView(DestroyAPIView):
    queryset = Center.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    http_method_names = ['delete']

    def get_object(self):
        try:
            return Center.objects.get(id=self.kwargs.get('id'))
        except Center.DoesNotExist:
            raise NotFound(detail="Bunday id dagi center topilmadi", code=404)

    def perform_destroy(self, instance):
        instance.delete()
        print(f"Center with id {instance.id} has been deleted.")

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Center muvaffaqiyatli o‘chirildi"}, status=status.HTTP_200_OK)
