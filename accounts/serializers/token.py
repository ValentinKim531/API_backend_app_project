from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, *args, **kwargs):
        data = super().validate(*args, **kwargs)

        if not self.user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {self.user.username}"
                          f" был деактивирован!"
            }, code='user_deleted')

        data['id'] = self.user.id
        data['username'] = self.user.username

        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])

        try:
            user = User.objects.get(
                pk=refresh.payload.get('user_id')
            )
        except ObjectDoesNotExist:
            raise serializers.ValidationError({
                'detail': f"Пользователь был удалён!"
            }, code='user_does_not_exists')

        if not user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {user.username} был архивирован!"
            }, code='user_deleted')

        data['id'] = user.id
        data['username'] = user.username

        return data
