from rest_batteries.mixins import (
    CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_batteries.viewsets import GenericViewSet
from rest_framework import serializers

from api.base.fields import PasswordField
from users.models import User
from users.services import create_user, delete_user, update_user


class UserSerializer(serializers.ModelSerializer):
    password = PasswordField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )


class UserCreateResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserSerializer()


class UserViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    request_action_serializer_classes = {
        'create': UserSerializer,
        'update': UserSerializer,
    }
    response_action_serializer_classes = {
        'create': UserCreateResponseSerializer,
        'retrieve': UserSerializer,
        'update': UserSerializer,
    }

    def perform_create(self, serializer):
        return {
            'token': 'randomusertoken',
            'user': create_user(**serializer.validated_data),
        }

    def perform_update(self, instance, serializer):
        return update_user(user=instance, **serializer.validated_data)

    def perform_destroy(self, instance, serializer=None):
        delete_user(user=instance)
