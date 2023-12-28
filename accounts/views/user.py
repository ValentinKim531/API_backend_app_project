import logging

from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import OTP, User
from accounts.serializers import UserSerializer, GetUserSerializer, UpdateUserSerializer, ChangePasswordAuthSerializer, \
    SetNewPasswordAuthSerializer, UserAvatarSerializer

logger = logging.getLogger(__name__)


class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['POST'],
        tags=['user']
    )
    def create(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            r = OTP.objects.filter(user=username).last()
            logger.warning("STARTED REGISTER")

            if r.verified:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)

                user = serializer.save()

                logger.warning('USER SAVED')
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            response = exception_handler(e, None)
            if response is not None:
                return Response(response.data, status=response.status_code)
            return Response(
                {'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class GetUserViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = User.objects.order_by('pk')
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer

    def get_current_user(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(instance=user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class AuthenticatedUserUpdate(GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = request.user
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'message': 'Пользователь успешно обновлен'})

    def perform_update(self, serializer):
        serializer.save()


class ChangeAuthenticatedUserPassword(ModelViewSet):
    serializer_class = ChangePasswordAuthSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=serializer_class,
        responses={201},
        methods=['POST'],
        tags=['user']
    )
    def change_password_auth(self, request):
        user = request.user
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        if check_password(password, user.password):
            user.set_password(new_password)
            user.save()
            return Response(
                {'status': 'Пароль изменен'}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'status': 'Неверный пароль'},
                status=status.HTTP_400_BAD_REQUEST
            )


class SetNewUserPassword(ModelViewSet):
    serializer_class = SetNewPasswordAuthSerializer
    queryset = User.objects.all()

    @extend_schema(
        request=serializer_class,
        responses={201},
        methods=['POST'],
        tags=['user']
    )
    def set_password_auth(self, request):
        try:
            username = request.data.get('username')
            r = OTP.objects.filter(user=username).last()
            logger.warning("STARTED SET NEW PASSWORD")
            if r.verified:
                user = get_object_or_404(
                    User.objects.all(), username=username
                )
                new_password = request.data.get('new_password')
                user.set_password(new_password)
                user.save()
                return Response(
                    {'status': 'Пароль изменен'}, status=status.HTTP_200_OK
                )
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            logger.exception(e)
            return Response(status=status.HTTP_403_FORBIDDEN)


class UserAvatarUpdate(GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = UserAvatarSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def update_avatar(self, request):
        user = request.user
        user.avatar = request.data.get('avatar')
        user.save()
        return Response(
            {'message': 'Аватар успешно обновлен'}, status=status.HTTP_200_OK
        )
