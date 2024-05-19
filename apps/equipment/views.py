from rest_framework import viewsets

from apps.equipment.models import Equipment
from apps.equipment.serializers import EquipmentSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    model = Equipment
    queryset = Equipment.objects.all().order_by("-title")
