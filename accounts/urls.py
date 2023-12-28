from django.urls import path

from .views import (
    CustomTokenObtainPairView, CustomTokenRefreshView,
    RegisterView, EmailView, GetUserViewSet, AuthenticatedUserUpdate,
    ChangeAuthenticatedUserPassword, SetNewUserPassword, UserAvatarUpdate
)


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view()),
    path('token/refresh/', CustomTokenRefreshView.as_view()),
    path('register/', RegisterView.as_view({'post': 'create'})),
    path('send_email/', EmailView.as_view({'post': 'send'})),
    path('verify_email/', EmailView.as_view({'post': 'verify'})),
    path('get/', GetUserViewSet.as_view({'get': 'get_current_user'})),
    path('update/', AuthenticatedUserUpdate.as_view({'put': 'update'})),
    path('update_avatar/',
         UserAvatarUpdate.as_view({'patch': 'update_avatar'})),
    path(
        'change_auth_password/',
        ChangeAuthenticatedUserPassword.as_view(
            {'post': 'change_password_auth'}
        )
    ),
    path('set_auth_new_password/',
         SetNewUserPassword.as_view({'post': 'set_password_auth'})),
]