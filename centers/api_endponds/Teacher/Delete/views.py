from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from centers.permissions import IsCenterAdmin

from centers.models import Teacher


class TeacherDeleteView(DestroyAPIView):
    queryset = Teacher.objects.all()
    permission_classes = [IsAuthenticated, IsCenterAdmin]
    http_method_names = ['delete']
    lookup_field = 'id'
    
    def get_object(self):
        try:
            return Teacher.objects.get(id=self.kwargs.get('id'))
        except Teacher.DoesNotExist:
            raise NotFound(detail='Uqituvchi topilmadi.', code=404)
        
    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Uqituvchi muvaffaqiyatli uchirildi.'})