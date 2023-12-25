from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from ..models import AdvantageMain


@admin.register(AdvantageMain)
class AdvantageMainAdmin(SummernoteModelAdmin):
    readonly_fields = ('top_background_image_preview',)
    fields = (
        'title','title_kz','title_en',
        'subtitle','subtitle_kz','subtitle_en',
        'top_background_image', 'top_background_image_preview'
    )

    def has_add_permission(self, request):
        count = self.model.objects.count()
        max_objects = 1
        if count >= max_objects:
            return False
        else:
            return True
    def top_background_image_preview(self, obj):
        if obj.top_background_image:
            return mark_safe(f'<img src = "{obj.top_background_image.url}" width="250px" height="350px"/>')
        return '-'

    top_background_image_preview.short_description = 'Предпросмотр изображения'
