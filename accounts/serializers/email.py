from rest_framework import serializers


class EmailVerifySerializer(serializers.Serializer):
    username = serializers.CharField()
    is_registration = serializers.BooleanField()


class EmailCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()


class EmailResultSerializer(serializers.Serializer):
    success = serializers.BooleanField()
