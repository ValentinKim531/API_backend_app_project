from rest_framework import serializers

from ..models import CallbackRequest


class CallbackRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallbackRequest
        fields = (
            'phone_number',
        )
