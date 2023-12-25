from django.conf import settings
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from ..models import RoomImage, Room


class RoomImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = RoomImage
        fields = ('image',)

    @extend_schema_field(serializers.URLField(required=False))
    def get_image(self, obj):
        try:
            url = str(settings.HOST_URL) + str(obj.room_image.url)
            return url
        except:
            return None


class RoomSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = (
            'title', 'subtitle', 'description', 'available',
            'price', 'room_images'
        )


class RoomKZSerializer(RoomSerializer):
    class Meta:
        model = Room
        fields = (
            'title', 'subtitle', 'description', 'available',
            'price', 'room_images'
        )
        extra_kwargs = {
            'title': {'source': 'title_kz'},
            'subtitle': {'source': 'subtitle_kz'},
            'description': {'source': 'description_kz'},
        }


class RoomENSerializer(RoomSerializer):
    class Meta:
        model = Room
        fields = (
            'title', 'subtitle', 'description', 'available',
            'price', 'room_images'
        )
        extra_kwargs = {
            'title': {'source': 'title_en'},
            'subtitle': {'source': 'subtitle_en'},
            'description': {'source': 'description_kz'},
        }
