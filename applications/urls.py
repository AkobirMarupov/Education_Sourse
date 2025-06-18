from django.urls import path

from applications.api_endpoinds.Application.Create.views import ApplicationCreateAPIView
from applications.api_endpoinds.Application.List.views import ApplicationListAPIView, ApplicationRetrievAPIView


urlpatterns = [
    path('applications/list/', ApplicationListAPIView.as_view(), name='applications-list'),
    path('applications/create/', ApplicationCreateAPIView.as_view(), name='applications-create'),
    path('applications/<int:id>/', ApplicationRetrievAPIView.as_view(), name='applications-retriev')
]