from django.urls import path
from student.api_endpoinds.Group.Create.views import StudentGroupCreateAPIView, MyGroupsAPIView

urlpatterns = [
    path('studentgroup/create/', StudentGroupCreateAPIView.as_view(), name='studentgroup-create'),
    path('my-groups/', MyGroupsAPIView.as_view(), name='my-groups'),
]
