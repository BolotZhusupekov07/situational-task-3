from django.contrib.auth.models import User
from rest_framework import viewsets

from apps.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all().order_by("id")
