from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from ..models import EventImage, Event


class EventImageInline(admin.TabularInline):
    model = EventImage
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.event_image:
            return mark_safe(f'<img src = "{obj.event_image.url}" width="250px" height="350px"/>')
        return '-'

    image_preview.short_description = 'Предпросмотр изображения'


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    inlines = [EventImageInline]
    fields = (
        'title','title_kz','title_en',
        'subtitle','subtitle_kz','subtitle_en',
        'description','description_kz','description_en',
        'available','price'
    )
