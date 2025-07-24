from django.urls import path
from account.api_endpoinds import (
    UserRegisterUserAPIView, UserRegisterConfirmAPIView,
    ProfileCreateAPIView, ProfileListrAPIView, ProfileListOneAPIView,
    ProfileDeleteAPIView, ProfileUpdateAPIView
)


urlpatterns = [
    # register
    path('register/', UserRegisterUserAPIView.as_view(), name='register-user'),
    path('register/confirm/', UserRegisterConfirmAPIView.as_view(), name='register-confirm'),

    #profile
    path('create', ProfileCreateAPIView.as_view(), name='profile-create'),
    path('update/<int:id>', ProfileUpdateAPIView.as_view(), name='profile-create'),
    path('list', ProfileListrAPIView.as_view(), name='profile-list'),
    path('create/<int:id>', ProfileListOneAPIView.as_view(), name='profile-retriev'),
    path('delete/<int:id>', ProfileDeleteAPIView.as_view(), name='profile-delete')
]