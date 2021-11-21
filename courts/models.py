from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Court(models.Model):
    manager_user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.name}\nlat:{self.latitude}\nlng: {self.longitude}}}'

class DateBooked(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.court.pk}-{self.date}'