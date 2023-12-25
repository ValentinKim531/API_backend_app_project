from django.db import models
from django.utils.translation import gettext_lazy as _


class AdvantageMain(models.Model):
    title = models.CharField(verbose_name='Заголовок')
    title_kz = models.CharField(verbose_name='Заголовок KZ', blank=True, null=True)
    title_en = models.CharField(verbose_name='Заголовок  EN', blank=True, null=True)

    subtitle = models.TextField(verbose_name='Подзаголовок')
    subtitle_kz = models.TextField(verbose_name='Подзаголовок KZ', blank=True, null=True)
    subtitle_en = models.TextField(verbose_name='Подзаголовок EN', blank=True, null=True)

    top_background_image = models.ImageField(verbose_name='Изображение верхнее', upload_to='advantage/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Главное преимущество')
        verbose_name_plural = _('Главное преимущество')