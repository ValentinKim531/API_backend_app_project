from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from ..models import CallbackRequest


@admin.register(CallbackRequest)
class CallbackRequestAdmin(SummernoteModelAdmin):
    fields = (
        'phone_number',
    )
