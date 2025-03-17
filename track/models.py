from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    prerequisites = ArrayField(models.CharField(max_length=100), default=list, blank=True)

    def __str__(self):
        return self.name