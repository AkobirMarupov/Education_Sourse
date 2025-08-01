from django.db import models
from django.contrib.auth import get_user_model
from centers.models import Center
from centers.models import Teacher
from courses.models import Course

User = get_user_model()

WEEKDAYS = (
    ('du', 'Dushanba'),
    ('se', 'Seshanba'),
    ('ch', 'Chorshanba'),
    ('pa', 'Payshanba'),
    ('ju', 'Juma'),
    ('sh', 'Shanba'),
    ('ya', 'Yakshanba'),
)

class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='groups')
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='groups')
    start_date = models.DateField()
    days = models.ManyToManyField('GroupDayTime', related_name='groups')

    def __str__(self):
        return self.name

class GroupDayTime(models.Model):
    weekday = models.CharField(max_length=2, choices=WEEKDAYS)
    time = models.TimeField()

    def __str__(self):
        return f"{self.get_weekday_display()} - {self.time.strftime('%H:%M')}"


class StudentGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_groups')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.group.name}"


    def __str__(self):
        return f"{self.user.email} - {self.group.name}"
