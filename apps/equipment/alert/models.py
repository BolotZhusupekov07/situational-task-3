from django.db import models

from apps.equipment.models import Equipment


class EquipmentAlert(models.Model):
    equipment = models.ForeignKey(Equipment, models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
