from django.db import models
from django.utils.translation import gettext_lazy as _


class Gallery(models.Model):
    title = models.CharField(verbose_name='Заголовок')
    title_kz = models.CharField(verbose_name='Заголовок KZ')
    title_en = models.CharField(verbose_name='Заголовок EN')

    subtitle = models.TextField(verbose_name='Подзаголовок', blank=True, null=True)
    subtitle_kz = models.TextField(verbose_name='Подзаголовок KZ', blank=True, null=True)
    subtitle_en = models.TextField(verbose_name='Подзаголовок EN', blank=True, null=True)

    class Meta:
        verbose_name = _('Галерея')
        verbose_name_plural = _('Галерея')


class GalleryImage(models.Model):
    gallery=models.ForeignKey(Gallery,verbose_name='Галерея',on_delete=models.CASCADE,related_name='gallery_images')
    gallery_image=models.ImageField(verbose_name='Изображение для галереи', upload_to='gallery/')

    class Meta:
        verbose_name='Изображение галереи'
        verbose_name_plural='Изображения галереи'

    def get_absolute_image_url(self):
        if self.gallery_image:
            return self.gallery_image.url
        return ''