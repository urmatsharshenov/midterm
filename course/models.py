from django.db import models


# Create your models here.

class Course(models.Model):
    teacher = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    time_from = models.CharField(max_length=10)
    time_to = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
