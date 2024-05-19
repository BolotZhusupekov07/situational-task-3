from django.utils import timezone
from django.db import models

from apps.equipment.models import Equipment


class EquipmentData(models.Model):
    equipment = models.ForeignKey(Equipment, models.CASCADE)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    speed = models.DecimalField(max_digits=10, decimal_places=2)
    pressure = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
