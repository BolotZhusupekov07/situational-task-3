from rest_framework import viewsets

from apps.equipment.data.models import EquipmentData
from apps.equipment.data.serializers import EquipmentDataSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EquipmentDataViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentDataSerializer
    model = EquipmentData
    queryset = EquipmentData.objects.all().order_by("-date")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["equipment"]
