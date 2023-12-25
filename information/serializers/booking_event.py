from django.utils import timezone
from rest_framework import serializers

from ..models import BookingEvent


class BookingEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingEvent
        fields = (
            'event', 'start_date', 'end_date',
            'customer_name', 'customer_contact', 'created_at'
        )

    def validate(self, data):
        """
        Проверка, что дата начала бронирования не раньше текущей даты
        и дата окончания бронирования после даты начала.
        """
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and start_date < timezone.now().date():
            raise serializers.ValidationError(
                {'start_date': 'Дата начала бронирования не может быть '
                               'раньше текущей даты.'})

        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError(
                {'end_date': 'Дата окончания бронирования должна быть после '
                             'даты начала бронирования.'})

        return data
