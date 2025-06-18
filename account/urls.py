from django.urls import path
from account.api_endpoinds import (
    UserRegisterUserAPIView, UserRegisterConfirmAPIView
)


urlpatterns = [
    # register
    path('register/', UserRegisterUserAPIView.as_view(), name='register-user'),
    path('register/confirm/', UserRegisterConfirmAPIView.as_view(), name='register-confirm')
]