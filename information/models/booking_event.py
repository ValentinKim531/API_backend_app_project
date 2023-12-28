from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from .event import Event



class BookingEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие', related_name='booking_events')
    start_date = models.DateField(verbose_name='Дата заезда')
    end_date = models.DateField(verbose_name='Дата выезда')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_booking', verbose_name='Пользователь', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.event} - {self.start_date} - {self.end_date} - {self.user}"

    class Meta:
        verbose_name = _('Бронирование мероприятия')
        verbose_name_plural = _('Бронирования мероприятий')