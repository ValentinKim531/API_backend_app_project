from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from ..models import Event
from ..serializers import EventSerializer, EventKZSerializer, EventENSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


@extend_schema(tags=['Events'])
class EventViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if "Accept-Language" in self.request.headers:
            if self.request.headers["Accept-Language"] == "kz":
                return EventKZSerializer
            elif self.request.headers["Accept-Language"] == "en":
                return EventENSerializer
            else:
                return EventSerializer
        else:
            return super(EventViewSet, self).get_serializer_class()
