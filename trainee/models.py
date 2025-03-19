from django.db import models
from django.contrib.auth.models import AbstractUser
from track.models import Track

class Trainee(AbstractUser):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email', 'track']
    USERNAME_FIELD = "username"
    def check_pre_requisites(self, courses_number):
        return isinstance(courses_number, int) and courses_number == self.track.prerequisites.count()


    def __str__(self):
        return self.username
