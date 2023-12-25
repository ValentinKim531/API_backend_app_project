from django.db import models
from django.utils.translation import gettext_lazy as _
import re
from django.core.exceptions import ValidationError
from .event import Event


# Валидация номера телефона
def validate_phone_number(value):
    if not re.match(r"^\+?1?\d{11,15}$", value):
        raise ValidationError('Номер телефона должен быть в формате +7XXXXXXXXXX')


class BookingEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие', related_name='booking_events')
    start_date = models.DateField(verbose_name='Дата заезда')
    end_date = models.DateField(verbose_name='Дата выезда')
    customer_name = models.CharField(verbose_name='Имя клиента', max_length=200)
    customer_contact = models.CharField(verbose_name='Контакт клиента', max_length=16, validators=[validate_phone_number])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.event} - {self.start_date} - {self.end_date} - {self.customer_name} - {self.customer_contact}"

    class Meta:
        verbose_name = _('Бронирование мероприятия')
        verbose_name_plural = _('Бронирования мероприятий')