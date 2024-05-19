from rest_framework import serializers

from apps.equipment.alert.models import EquipmentAlert


class EquipmentAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentAlert
        fields = [
            "id",
            "equipment",
            "description",
            "date",
        ]
        read_only_fields = ["id"]
