from django.db import models
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    title = models.CharField(verbose_name='Название')
    title_kz = models.CharField(verbose_name='Название KZ', blank=True, null=True)
    title_en = models.CharField(verbose_name='Название EN', blank=True, null=True)

    subtitle = models.CharField(verbose_name='Подзаголовок')
    subtitle_kz = models.CharField(verbose_name='Подзаголовок KZ', blank=True, null=True)
    subtitle_en = models.CharField(verbose_name='Подзаголовок EN', blank=True, null=True)

    description = models.TextField(verbose_name='Описание')
    description_kz = models.TextField(verbose_name='Описание KZ', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание EN', blank=True, null=True)
    main_image = models.ImageField(verbose_name='Основное изображение', upload_to='room/',
                                   blank=True, null=True)
    available = models.BooleanField(verbose_name='Доступность', default=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)


    def __str__(self):
        return self.title

    def get_main_image_url(self):
        # Если основное изображение задано, возвращаем его URL
        if self.main_image:
            return self.main_image.url
        # Если нет, возвращаем URL первого изображения из room_images
        # или пустую строку, если изображений нет
        return self.room_images.first().get_absolute_image_url() if self.room_images.exists() else ''

    class Meta:
        verbose_name = _('Номер')
        verbose_name_plural = _('Номера')


class RoomImage(models.Model):
    room=models.ForeignKey(Room,verbose_name='Связанный номер',on_delete=models.CASCADE,related_name='room_images')
    room_image=models.ImageField(verbose_name='Изображение номера', upload_to='room/')

    class Meta:
        verbose_name='Изображение номера'
        verbose_name_plural='Изображения номеров'

    def get_absolute_image_url(self):
        if self.room_image:
            return self.room_image.url
        return ''
