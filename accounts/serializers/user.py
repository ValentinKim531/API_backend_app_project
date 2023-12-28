from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=25,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'last_name', 'first_name',
            'phone_number', 'password'
        )

    def save(self):
        password = self.validated_data.pop('password', None)
        if password:
            self.validated_data['password'] = make_password(password)

        return super().save()


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'last_name', 'first_name', 'username', 'phone_number'
        )


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'phone_number', 'last_name', 'first_name'
        )


class ChangePasswordAuthSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()


class SetNewPasswordAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    new_password = serializers.CharField()


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', )
