from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from centers.models import Course


class CourseDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete']
    lookup_field = 'id'

    def get_object(self):
        try:
            return Course.objects.get(id=self.kwargs.get('id'))
        except Course.DoesNotExist:
            raise NotFound(detail = 'Corse Topilmadi.', code=404)
    
    def perform_destroy(self, instance):
        instance.delete()
        print(f"Center with id {instance.id} has been deleted.")

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Corse muvaffaqiyatli uchirildi.'})