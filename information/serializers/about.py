from django.conf import settings
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from ..models import About


class AboutSerializer(serializers.ModelSerializer):
    top_background_image = serializers.SerializerMethodField()
    middle_background_image = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = (
            'title', 'subtitle', 'brief_description',
            'detailed_description', 'top_background_image',
            'middle_background_image'
        )

    @extend_schema_field(serializers.URLField(required=False))
    def get_top_background_image(self, obj):
        try:
            url = str(settings.HOST_URL) + str(obj.top_background_image.url)
            return url
        except:
            return None

    @extend_schema_field(serializers.URLField(required=False))
    def get_middle_background_image(self, obj):
        try:
            url = str(settings.HOST_URL) + str(obj.middle_background_image.url)
            return url
        except:
            return None


class AboutKZSerializer(AboutSerializer):
    class Meta:
        model = About
        fields = (
            'title', 'subtitle', 'brief_description',
            'detailed_description', 'top_background_image', 'middle_background_image'
        )
        extra_kwargs = {
            'title': {'source': 'title_kz'},
            'subtitle': {'source': 'subtitle_kz'},
            'brief_description': {'source': 'brief_description_kz'},
            'detailed_description': {'source': 'detailed_description_kz'},
        }


class AboutENSerializer(AboutSerializer):
    class Meta:
        model = About
        fields = (
            'title', 'subtitle', 'brief_description',
            'detailed_description', 'top_background_image', 'middle_background_image'
        )
        extra_kwargs = {
            'title': {'source': 'title_en'},
            'subtitle': {'source': 'subtitle_en'},
            'brief_description': {'source': 'brief_description_en'},
            'detailed_description': {'source': 'detailed_description_en'},
        }
