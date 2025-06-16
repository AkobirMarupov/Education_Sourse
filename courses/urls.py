from django.urls import path
from django.conf.urls.static import static


from courses.api_endpoinds import (
    CourseCreateAPIView, CourseDeleteAPIView, CourseDetailAPIView,
    CourseListAPIView, CourseUpdateAPIView
)


urlpatterns = [

    # course
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('course/<int:id>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('course/update/<int:id>/', CourseUpdateAPIView.as_view(), name='course-update'),
    path('course/delete/<int:id>/', CourseDeleteAPIView.as_view(), name='course-delete'),
] 

