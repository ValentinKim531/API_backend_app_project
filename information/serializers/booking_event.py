from django.utils import timezone
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from ..models import BookingEvent


class BookingEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingEvent
        fields = (
            'event', 'start_date', 'end_date',
            'user', 'created_at'
        )

    def validate(self, data):
        """
        Проверка, что дата начала бронирования не раньше текущей даты
        и дата окончания бронирования после даты начала.
        """
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language') if request else None

        if start_date and start_date < timezone.now().date():
            if lang == "" or lang is None:
                error_msg = _(
                    'Дата начала бронирования не может быть раньше текущей '
                    'даты.'
                )
                raise serializers.ValidationError({'start_date': error_msg})
            elif lang == "kz":
                error_msg = _(
                    'KAZAK Дата начала бронирования не может быть раньше '
                    'текущей даты.'
                )
                raise serializers.ValidationError({'start_date': error_msg})
            elif lang == "en":
                error_msg = _(
                    'ENGLISH Дата начала бронирования не может быть раньше '
                    'текущей даты.'
                )
                raise serializers.ValidationError({'start_date': error_msg})

        if start_date and end_date and end_date <= start_date:
            if lang == "" or lang is None:
                error_msg = _(
                    'RUS Дата окончания бронирования должна быть после даты '
                    'начала бронирования.'
                )
                raise serializers.ValidationError({'end_date': error_msg})
            elif lang == "kz":
                error_msg = _(
                    'KAZAK Дата окончания бронирования должна быть после даты '
                    'начала бронирования.'
                )
                raise serializers.ValidationError({'start_date': error_msg})
            elif lang == "en":
                error_msg = _(
                    'ENGLISH Дата окончания бронирования должна быть после даты '
                    'начала бронирования.'
                )
                raise serializers.ValidationError({'start_date': error_msg})

        return data
