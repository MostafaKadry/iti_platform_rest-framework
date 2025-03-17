from django.db import models
from track.models import Track
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    track = models.ManyToManyField(Track, related_name='courses')
    hours = models.IntegerField(null=False)
    def __str__(self):
        return self.name