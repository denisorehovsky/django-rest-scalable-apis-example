from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework import serializers

from api.base.fields import PasswordField
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = PasswordField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )


class UserViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
