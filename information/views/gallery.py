from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Gallery
from ..serializers import GallerySerializer, GalleryKZSerializer, GalleryENSerializer


class GalleryViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = GallerySerializer

    def get_object(self):
        return Gallery.objects.first()

    @extend_schema(
        methods=['GET'],
        tags=['Gallery']
    )
    def get_gallery(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if "Accept-Language" in self.request.headers:
            if self.request.headers["Accept-Language"] == "kz":
                return GalleryKZSerializer
            elif self.request.headers["Accept-Language"] == "en":
                return GalleryENSerializer
            else:
                return GallerySerializer
        else:
            return super(GalleryViewSet, self).get_serializer_class()
