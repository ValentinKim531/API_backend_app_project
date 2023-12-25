from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import BookingEvent
from ..serializers import BookingEventSerializer


@extend_schema(tags=['BookingEvents'])
class BookingEventViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = BookingEvent.objects.all()
    serializer_class = BookingEventSerializer
