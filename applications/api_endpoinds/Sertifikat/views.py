from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from applications.models import Certificate
from applications.api_endpoinds.Sertifikat.serializers import CertificateSerializer
from applications.utils.certificate_generator import generate_certificate_pdf


class CertificateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CertificateRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]


class CertificateApproveAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        try:
            certificate = Certificate.objects.get(pk=pk)
        except Certificate.DoesNotExist:
            return Response({"detail": "Sertifikat topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        if certificate.certificate_file:
            return Response({"detail": "Sertifikat allaqachon yaratilgan."}, status=status.HTTP_400_BAD_REQUEST)

        generate_certificate_pdf(certificate)

        return Response({
            "detail": "Sertifikat PDF ko‘rinishda yaratildi.",
            "certificate_url": certificate.certificate_file.url
        }, status=status.HTTP_201_CREATED)
