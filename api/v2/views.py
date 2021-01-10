from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import serializers, status

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


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request_serializer = UserSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        user = create_user(**request_serializer.validated_data)

        response_serializer = UserCreateResponseSerializer({
            'token': 'randomusertoken',
            'user': user,
        })
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED
        )

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        request_serializer = UserSerializer(
            user, data=request.data, partial=True
        )
        request_serializer.is_valid(raise_exception=True)

        user = update_user(user=user, **request_serializer.validated_data)

        response_serializer = UserSerializer(user)
        return Response(response_serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        delete_user(user=user)
        return Response(status=status.HTTP_204_NO_CONTENT)
