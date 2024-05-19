from rest_framework import viewsets

from apps.equipment.alert.models import EquipmentAlert
from apps.equipment.alert.serializers import EquipmentAlertSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EquipmentAlertViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentAlertSerializer
    model = EquipmentAlert
    queryset = EquipmentAlert.objects.all().order_by("-date")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["equipment"]
