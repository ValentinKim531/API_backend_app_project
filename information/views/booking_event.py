from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from ..models import BookingEvent
from ..serializers import BookingEventSerializer


@extend_schema(tags=['BookingEvents'])
class BookingEventViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = BookingEvent.objects.all()
    serializer_class = BookingEventSerializer

    def create(self, request, *args, **kwargs):
        context = {'request': request}
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)