from django.db import models
from django.utils.translation import gettext_lazy as _



class CallbackRequest(models.Model):
    phone_number = models.CharField(max_length=16, verbose_name='Номер телефона')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Звонок для ({self.phone_number})"

    class Meta:
        verbose_name = _('Заказ звонка')
        verbose_name_plural = _('Заказы звонков')