from django.conf import settings
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from ..models import AdvantageMain


class AdvantageMainSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AdvantageMain
        fields = (
            'title', 'subtitle', 'image'
        )

    @extend_schema_field(serializers.URLField(required=False))
    def get_image(self, obj):
        try:
            url = str(settings.HOST_URL) + str(obj.top_background_image.url)
            return url
        except:
            return None


class AdvantageMainKZSerializer(AdvantageMainSerializer):
    class Meta:
        model = AdvantageMain
        fields = (
            'title', 'subtitle', 'image'
        )
        extra_kwargs = {
            'title': {'source': 'title_kz'},
            'subtitle': {'source': 'subtitle_kz'},
        }


class AdvantageMainENSerializer(AdvantageMainSerializer):
    class Meta:
        model = AdvantageMain
        fields = (
            'title', 'subtitle', 'image'
        )
        extra_kwargs = {
            'title': {'source': 'title_en'},
            'subtitle': {'source': 'subtitle_en'},
        }
