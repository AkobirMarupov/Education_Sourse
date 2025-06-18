from django.db import models
from django.conf import settings

from common.models import BaseModel



class Application(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    center = models.ForeignKey(
        'centers.Center',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    teacher = models.ForeignKey('centers.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return str(self.student)
