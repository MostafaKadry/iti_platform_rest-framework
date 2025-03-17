from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from track.models import Track

class TraineeManager(BaseUserManager):
    def create_user(self, username, password=None, track=None, **extra_fields):
        if not username:
            raise ValueError("The Username field is required")

        user = self.model(username=username, track=track, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class Trainee(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Required for admin access
    is_superuser = models.BooleanField(default=False)  # Required for superuser

    objects = TraineeManager()

    USERNAME_FIELD = 'username'  # Used for authentication
    REQUIRED_FIELDS = []  # Other required fields when creating superusers

    def check_pre_requisites(self, courses_number):
        return isinstance(courses_number, int) and courses_number == self.track.prerequisites.count()

    def __str__(self):
        return self.username
