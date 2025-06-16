from django.urls import path
from centers.api_endponds import(
    CenterCreateAPIView, CenterListAPIView, CenterDetailAPIView, 
    CenterUpdateAPIView, CenterDeleteAPIView,
    LocationsListAPIView, LocationDetailAPIView, LocationCreateAPIView,
    TeacherCreateAPIView, TeacherDeleteView, TeacherRetriAPIView, 
    TeacherUpdateView, TeasherListAPIView
)

urlpatterns = [
    # Center
    path('centers/', CenterListAPIView.as_view(), name='center-list'),
    path('centers/<int:id>/', CenterDetailAPIView.as_view(), name='center-detail'),
    path('centers/create/', CenterCreateAPIView.as_view(), name='center-create'),
    path('centers/update/<int:id>/', CenterUpdateAPIView.as_view(), name='center-update'),
    path('centers/delete/<int:id>/', CenterDeleteAPIView.as_view(), name='center-delete'),

    
    # Teacher
    path('teachers/', TeasherListAPIView.as_view(), name='teacher-list'),
    path('teachers/create/', TeacherCreateAPIView.as_view(), name='teacher-create'),
    path('teachers/<int:id>/', TeacherRetriAPIView.as_view(), name='teacher-detail'),
    path('teachers/update/<int:id>/', TeacherUpdateView.as_view(), name='teacher-update'),
    path('teachers/delete/<int:id>/', TeacherDeleteView.as_view(), name='teacher-delete'),

    # Location
    path('locations/', LocationsListAPIView.as_view(), name='location-list'),
    path('locations/<int:id>/', LocationDetailAPIView.as_view(), name='location-detail'),
    path('locations/create/', LocationCreateAPIView.as_view(), name='location-create'),
]