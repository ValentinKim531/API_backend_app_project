from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    address = models.CharField(verbose_name='Адрес')
    address_kz = models.CharField(verbose_name='Адрес KZ', blank=True, null=True)
    address_en = models.CharField(verbose_name='Адрес EN', blank=True, null=True)

    phone = models.CharField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')


    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')


class SocialNetwork(models.Model):
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='social_networks', verbose_name='Социальные сети'
    )
    icon = models.ImageField(verbose_name='Иконка')
    link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return f'Социальная сеть №{self.pk}'

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'