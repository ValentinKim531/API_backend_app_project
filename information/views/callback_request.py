from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import CallbackRequest
from ..serializers import CallbackRequestSerializer


@extend_schema(tags=['CallbackRequest'])
class CallbackRequestViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = CallbackRequest.objects.all()
    serializer_class = CallbackRequestSerializer
