from django.conf import settings
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from ..models import EventImage, Event


class EventImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = EventImage
        fields = ('image',)

    @extend_schema_field(serializers.URLField(required=False))
    def get_image(self, obj):
        try:
            url = str(settings.HOST_URL) + str(obj.event_image.url)
            return url
        except:
            return None


class EventSerializer(serializers.ModelSerializer):
    event_images = EventImageSerializer(many=True)

    class Meta:
        model = Event
        fields = (
            'title', 'subtitle', 'description', 'available',
            'price', 'event_images'
        )


class EventKZSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = (
            'title', 'subtitle', 'description', 'available',
            'price', 'event_images'
        )
        extra_kwargs = {
            'title': {'source': 'title_kz'},
            'subtitle': {'source': 'subtitle_kz'},
            'description': {'source': 'description_kz'},
        }


class EventENSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = (
            'title', 'subtitle', 'description', 'available',
            'price', 'event_images'
        )
        extra_kwargs = {
            'title': {'source': 'title_en'},
            'subtitle': {'source': 'subtitle_en'},
            'description': {'source': 'description_kz'},
        }
