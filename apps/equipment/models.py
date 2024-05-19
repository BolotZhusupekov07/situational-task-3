from django.db import models


class EquipmentType(models.TextChoices):
    OUTDOOR = "OUTDOOR", "Outdoor"
    INDOOR = "INDOOR", "Indoor"
    ALL_PURPOSE = "ALL_PURPOSE", "All Purpose"


class EquipmentStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    DAMAGED = "DAMAGED", "Damaged"
    IN_REPAIR = "IN_REPAIR", "In Repair"


class Equipment(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(
        choices=EquipmentType.choices, default=EquipmentType.ALL_PURPOSE
    )
    status = models.CharField(
        choices=EquipmentStatus.choices, default=EquipmentStatus.ACTIVE
    )
    model = models.CharField(max_length=255)
    installation_date = models.DateTimeField()
