from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(verbose_name='Название')
    title_kz = models.CharField(verbose_name='Название KZ', blank=True, null=True)
    title_en = models.CharField(verbose_name='Название EN', blank=True, null=True)

    subtitle = models.CharField(verbose_name='Подзаголовок')
    subtitle_kz = models.CharField(verbose_name='Подзаголовок KZ', blank=True, null=True)
    subtitle_en = models.CharField(verbose_name='Подзаголовок EN', blank=True, null=True)

    description = models.TextField(verbose_name='Описание')
    description_kz = models.TextField(verbose_name='Описание KZ', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание EN', blank=True, null=True)

    available = models.BooleanField(verbose_name='Доступность', default=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')


class EventImage(models.Model):
    event=models.ForeignKey(Event,verbose_name='Связанный номер', on_delete=models.CASCADE, related_name='event_images')
    event_image=models.ImageField(verbose_name='Изображение номера', upload_to='event/')

    class Meta:
        verbose_name='Изображение мероприятия'
        verbose_name_plural='Изображения мероприятий'

    def get_absolute_image_url(self):
        if self.event_image:
            return self.event_image.url
        return ''