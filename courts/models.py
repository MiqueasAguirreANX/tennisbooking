from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Court(models.Model):
    manager_user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)