from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from accounts.serializers import EmailVerifySerializer, EmailCodeSerializer, EmailResultSerializer
from accounts.service import send_email, verify_email


class EmailView(ModelViewSet):

    @extend_schema(
        request=EmailVerifySerializer,
        methods=['POST'],
        tags=['user']
    )
    def send(self, request):
        language = self.request.headers.get("Accept-Language", "ru")
        if (request.data.get('is_registration') and
                User.objects.filter(username=request.data.get('username')).exists()):
            if language == "kz":
                return Response(
                    data={'error':
                              'Мұндай поштасы бар пайдаланушы қазірдің өзінде бар'},
                            status=status.HTTP_400_BAD_REQUEST)
            elif language == "en":
                return Response(
                    data={'error': 'A user with such an email already exists'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    data={'error': 'Пользователь с такой почтой уже существует'},
                                status=status.HTTP_400_BAD_REQUEST)
        send_email(request, language)
        return Response(status=status.HTTP_200_OK)

    @extend_schema(
        request=EmailCodeSerializer,
        responses={200: EmailResultSerializer},
        methods=['POST'],
        tags=['user']
    )
    def verify(self, request):
        r = verify_email(request)
        if r['success']:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
