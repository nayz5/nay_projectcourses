from django.db import models
import datetime
from datetime import timedelta
from django.utils import timezone


class allCourses(models.Model):
    course_name = models.CharField(max_length=500)
    instructor_name = models.CharField(max_length=500)
    started_from = models.DateTimeField('started from')

    def published_recently(self):
        return self.started_from >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.course_name


class details(models.Model):
    course = models.ForeignKey(allCourses, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.course_type
