from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import AdvantageMain
from ..serializers import AdvantageMainSerializer, AboutSerializer, AdvantageMainKZSerializer, \
    AdvantageMainENSerializer


@extend_schema(tags=['AdvantageMain'])
class AdvantageMainViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = AdvantageMainSerializer

    def get_object(self):
        return AdvantageMain.objects.first()

    @extend_schema(
        request=AboutSerializer,
        methods=['GET'],
        tags=['AdvantageMain']
    )
    def get_about(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if "Accept-Language" in self.request.headers:
            if self.request.headers["Accept-Language"] == "kz":
                return AdvantageMainKZSerializer
            elif self.request.headers["Accept-Language"] == "en":
                return AdvantageMainENSerializer
            else:
                return AdvantageMainSerializer
        else:
            return super(AdvantageMainViewSet, self).get_serializer_class()
