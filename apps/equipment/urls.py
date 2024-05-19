from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.equipment import views
from apps.equipment.data.urls import router as data_router
from apps.equipment.alert.urls import router as alerts_router

router = DefaultRouter()
router.register(
    r"api/equipments", views.EquipmentViewSet, basename="equipment"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(data_router.urls)),
    path("", include(alerts_router.urls)),
]
