from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Contact
from ..serializers import ContactSerializer, ContactKZSerializer, ContactENSerializer


class ContactViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = ContactSerializer

    def get_object(self):
        return Contact.objects.first()

    @extend_schema(
        request=ContactSerializer,
        methods=['GET'],
        tags=['Contacts']
    )
    def get_contacts(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if "Accept-Language" in self.request.headers:
            if self.request.headers["Accept-Language"] == "kz":
                return ContactKZSerializer
            elif self.request.headers["Accept-Language"] == "en":
                return ContactENSerializer
            else:
                return ContactSerializer
        else:
            return super(ContactViewSet, self).get_serializer_class()
