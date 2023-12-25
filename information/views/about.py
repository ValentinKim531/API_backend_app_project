from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import About
from ..serializers import AboutSerializer, AboutKZSerializer, AboutENSerializer


class AboutViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()

    @extend_schema(
        methods=['GET'],
        tags=['About']
    )
    def get_about(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if "Accept-Language" in self.request.headers:
            if self.request.headers["Accept-Language"] == "kz":
                return AboutKZSerializer
            elif self.request.headers["Accept-Language"] == "en":
                return AboutENSerializer
            else:
                return AboutSerializer
        else:
            return super(AboutViewSet, self).get_serializer_class()
