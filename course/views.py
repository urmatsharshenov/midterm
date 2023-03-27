from django.views.generic import ListView

from course import models


class CourseListAPIView(ListView):
    queryset = models.Course.objects.all()
    template_name = "courses.html"
