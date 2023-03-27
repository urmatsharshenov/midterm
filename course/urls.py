from django.urls import path
from course.views import CourseListAPIView


urlpatterns = [
    path("list", CourseListAPIView.as_view())
]
