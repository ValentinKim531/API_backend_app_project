from django.db import models
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    title = models.CharField(verbose_name='Заголовок')
    title_kz = models.CharField(verbose_name='Заголовок KZ', blank=True, null=True)
    title_en = models.CharField(verbose_name='Заголовок EN', blank=True, null=True)

    subtitle = models.CharField(verbose_name='Пододзаголовок')
    subtitle_kz = models.CharField(verbose_name='Пододзаголовок KZ', blank=True, null=True)
    subtitle_en = models.CharField(verbose_name='Пододзаголовок EN', blank=True, null=True)

    brief_description = models.CharField(verbose_name='Краткое описание')
    brief_description_kz = models.CharField(verbose_name='Краткое описание KZ', blank=True, null=True)
    brief_description_en = models.CharField(verbose_name='Краткое описание EN', blank=True, null=True)

    detailed_description = models.TextField(verbose_name='Подробное описание')
    detailed_description_kz = models.TextField(verbose_name='Подробное описание KZ', blank=True, null=True)
    detailed_description_en = models.TextField(verbose_name='Подробное описание EN', blank=True, null=True)

    top_background_image = models.ImageField(verbose_name='Изображение верхнее', upload_to='about/', blank=True, null=True)
    middle_background_image = models.ImageField(verbose_name='Изображение в середине', upload_to='about/', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')
