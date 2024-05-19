from rest_framework import serializers

from apps.equipment.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            "id",
            "title",
            "type",
            "status",
            "model",
            "installation_date",
        ]
        read_only_fields = ["id"]
