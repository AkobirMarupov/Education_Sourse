from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from applications.models import Application


class ApplicationDeleteAPIView(DestroyAPIView):
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    http_method_names = ['delete']

    def get_object(self):
        try:
            return Application.objects.get(id=self.kwargs.get('id'))
        except Application.DoesNotExist:
            raise NotFound(detail="Bunday id dagi ariza topilmadi", code=404)

    def perform_destroy(self, instance):
        instance.delete()
        print(f"Center with id {instance.id} has been deleted.")

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Ariza muvaffaqiyatli o‘chirildi"}, status=status.HTTP_200_OK)