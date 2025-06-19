from django.db import models
from django.conf import settings
from django.utils import timezone

from account.models import Profile
from centers.models import Center
from courses.models import Course
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



class Certificate(BaseModel):
    student = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='certificates'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='certificates'
    )
    center = models.ForeignKey(
        Center,
        on_delete=models.CASCADE,
        related_name='certificates'
    )
    issue_date = models.DateField(default=timezone.now)
    certificate_file = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        student_name = getattr(self.student, 'full_name', str(self.student))
        course_title = getattr(self.course, 'title', str(self.course))
        return f"{student_name} - {course_title}"
