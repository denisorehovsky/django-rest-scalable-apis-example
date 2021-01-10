from rest_framework.mixins import (
    DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import serializers, status

from api.base.fields import PasswordField
from users.models import User
from users.services import create_user


class UserSerializer(serializers.ModelSerializer):
    password = PasswordField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )

    def create(self, validated_data):
        return create_user(**validated_data)


class UserCreateResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserSerializer()


class UserViewSet(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request_serializer = UserSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        request_serializer.save()

        response_serializer = UserCreateResponseSerializer({
            'token': 'randomusertoken',
            'user': request_serializer.instance,
        })
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED
        )
