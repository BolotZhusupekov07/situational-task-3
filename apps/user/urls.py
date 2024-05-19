from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.user import views

router = DefaultRouter()
router.register(r"api/users", views.UserViewSet, basename="user")

urlpatterns = [path("", include(router.urls))]
