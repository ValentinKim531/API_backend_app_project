from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from ..models import BookingEvent


@admin.register(BookingEvent)
class BookingEventAdmin(SummernoteModelAdmin):
    fields = (
        'event','start_date','end_date',
        'user'
    )
