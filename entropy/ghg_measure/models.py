from ast import mod
from django.db import models

class EmissionManager(models.Model):
    name = models.CharField(max_length=100)
    daily_average = models.DecimalField(max_digits=100, decimal_places=4)
    updated = models.BooleanField(null=True)