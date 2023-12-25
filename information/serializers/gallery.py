from django.conf import settings
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from ..models import GalleryImage, Gallery


class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ('image',)

    @extend_schema_field(serializers.URLField(required=False))
    def get_image(self, obj):
        try:
            url = str(settings.HOST_URL) + str(obj.gallery_image.url)
            return url
        except:
            return None


class GallerySerializer(serializers.ModelSerializer):
    gallery_images = GalleryImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = (
            'title', 'subtitle', 'gallery_images'
        )


class GalleryKZSerializer(GallerySerializer):
    class Meta:
        model = Gallery
        fields = (
            'title', 'subtitle', 'gallery_images'
        )
        extra_kwargs = {
            'title': {'source': 'title_kz'},
            'subtitle': {'source': 'subtitle_kz'},
        }


class GalleryENSerializer(GallerySerializer):
    class Meta:
        model = Gallery
        fields = (
            'title', 'subtitle', 'gallery_images'
        )
        extra_kwargs = {
            'title': {'source': 'title_en'},
            'subtitle': {'source': 'subtitle_en'},
        }
