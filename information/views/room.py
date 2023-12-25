from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Room
from ..serializers import RoomSerializer, RoomKZSerializer, RoomENSerializer
from ..views.event import StandardResultsSetPagination


@extend_schema(tags=['Rooms'])
class RoomViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Room.objects.all().order_by('id')
    serializer_class = RoomSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if "Accept-Language" in self.request.headers:
            if self.request.headers["Accept-Language"] == "kz":
                return RoomKZSerializer
            elif self.request.headers["Accept-Language"] == "en":
                return RoomENSerializer
            else:
                return RoomSerializer
        else:
            return super(RoomViewSet, self).get_serializer_class()
