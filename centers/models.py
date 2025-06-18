from django.db import models
from django.utils import timezone
from datetime import timedelta

from common.models import BaseModel
from courses.models import Course


class Center(BaseModel):
    PAYMENT_STATUS_CHOICES = (
        ('free', 'Bepul'),
        ('premium', 'Premium'),
        ('gold', 'Gold'),
    )

    owner = models.ForeignKey('account.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=65, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='free'
    )

    def __str__(self):
        return self.name



class Teacher(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('online', 'online'),
        ('offline', 'offline')
    )
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='teachers')
    full_name = models.CharField(max_length=255)
    bio = models.TextField()
    experience_years = models.PositiveIntegerField()
    subject = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='teachers')
    teaching_method = models.CharField(max_length=255,
        choices=PAYMENT_STATUS_CHOICES,
        default='lesson1')
    photo = models.ImageField(upload_to='teachers/photos/', null=True, blank=True)


    def __str__(self):
        return self.full_name


class Location(BaseModel):
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=255)  
    address = models.TextField(blank=True, null=True) 
    latitude = models.DecimalField(max_digits=16, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=8, blank=True, null=True)


    def __str__(self):
        return f"{self.center.name} - {self.name}"

    @property
    def google_map_url(self):
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        return None



class Story(BaseModel):
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='stories')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='stories', null=True, blank=True)
    image = models.ImageField(upload_to='stories/images/', null=True, blank=True)
    video = models.FileField(upload_to='stories/videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=timezone.now() + timedelta(hours=24))


    def __str__(self):
        return f"{self.title} - {self.center.name}"

    def is_expired(self):
        return timezone.now() > self.expires_at

    def view_count(self):
        return self.views.count()