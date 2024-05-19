from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.equipment.data import views

router = DefaultRouter()
router.register(
    r"api/equipments-data",
    views.EquipmentDataViewSet,
    basename="equipment-data",
)

urlpatterns = [path("", include(router.urls))]
