from .email import EmailView
from .token import CustomTokenObtainPairView, CustomTokenRefreshView
from .user import (
    RegisterView, GetUserViewSet, AuthenticatedUserUpdate,
    ChangeAuthenticatedUserPassword, SetNewUserPassword, UserAvatarUpdate
)