from rest_framework import serializers

from apps.equipment.data.models import EquipmentData


class EquipmentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentData
        fields = [
            "id",
            "equipment",
            "temperature",
            "speed",
            "pressure",
            "date",
        ]
        read_only_fields = ["id", "date"]
