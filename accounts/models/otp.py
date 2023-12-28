import string
from random import choice

from django.db import models


class OTP(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=4)
    user = models.CharField(verbose_name="Почта", max_length=255, default="")
    verified = models.BooleanField(verbose_name='Подтвержден', default=False)

    @staticmethod
    def generate_code():
        chars = string.digits
        return ''.join(choice(chars) for _ in range(4))
