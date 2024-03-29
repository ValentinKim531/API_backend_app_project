from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from ..models import Advantage


@admin.register(Advantage)
class AdvantageAdmin(SummernoteModelAdmin):
    readonly_fields = ('image_preview',)
    fields = (
        'title','title_kz','title_en',
        'subtitle','subtitle_kz','subtitle_en',
        'image', 'image_preview'
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src = "{obj.image.url}" width="250px" height="350px"/>')
        return '-'

    image_preview.short_description = 'Предпросмотр изображения'
