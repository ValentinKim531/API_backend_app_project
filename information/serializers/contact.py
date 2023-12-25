from django.conf import settings
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from ..models import SocialNetwork, Contact


class SocialNetworkSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = SocialNetwork
        fields = ('icon', 'link')

    @extend_schema_field(serializers.URLField(required=False))
    def get_icon(self, obj):
        try:
            url = str(settings.HOST_URL) + str(obj.icon.url)
            return url
        except:
            return None


class ContactSerializer(serializers.ModelSerializer):
    social_networks = SocialNetworkSerializer(many=True)

    class Meta:
        model = Contact
        fields = (
            'address', 'phone', 'email', 'social_networks'
        )


class ContactKZSerializer(ContactSerializer):
    class Meta:
        model = Contact
        fields = (
            'address', 'phone', 'email', 'networks'
        )
        extra_kwargs = {
            'address': {'source': 'address_kz'},
        }


class ContactENSerializer(ContactSerializer):
    class Meta:
        model = Contact
        fields = (
            'address', 'phone', 'email', 'networks'
        )
        extra_kwargs = {
            'address': {'source': 'address_en'},
        }
