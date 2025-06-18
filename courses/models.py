from django.db import models

from common.models import BaseModel


class Course(BaseModel):
    PAYMENT_STATUS_CHOICES = (
        ('3 oy', '3 oy'),
        ('6 oy', '6 oy'),
        ('8 0y', '8 oy'),
    )
    PAYMENT_STATUS_DATE = (
        ('3 kun', '3 kun'),
        ('5 kun', '5 kun')
    )
    center = models.ForeignKey('centers.Center', on_delete=models.RESTRICT, related_name='courses')
    title = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='vaqt1'
    )
    price = models.BigIntegerField(null=False, blank=False)
    language = models.CharField(max_length=100, null=True, blank=True)
    schedule = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_DATE,
        default='kun1'
    )

    def __str__(self):
        return self.title
    
    
class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=255)
    link = models.URLField(help_text="YouTube video havolasi")

    class Meta:
        verbose_name = 'Course Resource'
        verbose_name_plural = 'Course Resources'

    def __str__(self):
        return f"{self.course.title} - {self.title}"


