from django.urls import path

from applications.api_endpoinds.Application.Create.views import ApplicationCreateAPIView
from applications.api_endpoinds.Application.List.views import ApplicationListAPIView, ApplicationRetrievAPIView
from applications.api_endpoinds.Application.Delete.views import ApplicationDeleteAPIView
from applications.api_endpoinds.Application.Update.views import ApplicationUpdateAPIView
from applications.api_endpoinds.Sertifikat.views import CertificateListCreateAPIView, CertificateRetrieveAPIView, CertificateApproveAPIView


urlpatterns = [
    path('applications/list/', ApplicationListAPIView.as_view(), name='applications-list'),
    path('applications/create/', ApplicationCreateAPIView.as_view(), name='applications-create'),
    path('applications/<int:id>/', ApplicationRetrievAPIView.as_view(), name='applications-retriev'),
    path('applications/update/<int:id>/', ApplicationUpdateAPIView.as_view(), name='applications-update'),
    path('applications/delete/<int:id>/', ApplicationDeleteAPIView.as_view(), name='applications-delete'),

    path('certificat/', CertificateListCreateAPIView.as_view(), name='certificate-list-create'),
    path('certificat/<int:pk>/', CertificateRetrieveAPIView.as_view(), name='certificate-detail'),
    path('certificat/<int:pk>/approve/', CertificateApproveAPIView.as_view(), name='certificate-approve'),
]