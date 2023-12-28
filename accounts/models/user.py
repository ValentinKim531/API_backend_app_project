import re

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


# Валидация номера телефона
def validate_phone_number(value):
    if not re.match(r"^\+?1?\d{11,15}$", value):
        raise ValidationError(
            'Номер телефона должен быть в формате +7XXXXXXXXXX'
        )


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    IS_ACTIVE = (
        (True, 'Не заблокирован'),
        (False, 'Заблокирован'),
    )

    id = models.AutoField(primary_key=True)
    username = models.EmailField(_('Почта'), max_length=50, unique=True)
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    phone_number = models.CharField(
        _('Номер телефона'), max_length=15, unique=True,
        validators=[validate_phone_number]
    )
    avatar = models.ImageField(
        upload_to='avatars/', verbose_name='Аватар',
        null=True, blank=True
    )
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_active = models.BooleanField(
        default=True,
        choices=IS_ACTIVE,
        verbose_name='Статус доступа',
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
