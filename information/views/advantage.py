from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Advantage
from ..serializers import AdvantageSerializer, AdvantageKZSerializer, AdvantageENSerializer
from ..views.event import StandardResultsSetPagination


@extend_schema(tags=['Advantages'])
class AdvantageViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Advantage.objects.all().order_by('id')
    serializer_class = AdvantageSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if "Accept-Language" in self.request.headers:
            if self.request.headers["Accept-Language"] == "kz":
                return AdvantageKZSerializer
            elif self.request.headers["Accept-Language"] == "en":
                return AdvantageENSerializer
            else:
                return AdvantageSerializer
        else:
            return super(AdvantageViewSet, self).get_serializer_class()
