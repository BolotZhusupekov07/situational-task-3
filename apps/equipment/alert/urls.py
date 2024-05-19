from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.equipment.alert import views

router = DefaultRouter()
router.register(
    r"api/equipments-alerts",
    views.EquipmentAlertViewSet,
    basename="equipment-alerts",
)

urlpatterns = [path("", include(router.urls))]
