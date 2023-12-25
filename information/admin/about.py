from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from ..models import About
from django_summernote.models import Attachment


admin.site.unregister(Attachment)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    readonly_fields = ('top_background_image_preview', 'middle_background_image_preview')
    fields = (
        'title','title_kz','title_en',
        'subtitle','subtitle_kz','subtitle_en',
        'brief_description','brief_description_kz','brief_description_en',
        'detailed_description','detailed_description_kz','detailed_description_en',
        'top_background_image','top_background_image_preview',
        'middle_background_image','middle_background_image_preview'
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
            return mark_safe(f'<img src = "{obj.top_background_image.url}" width="100%" height="500px"/>')
        return '-'

    def middle_background_image_preview(self, obj):
        if obj.middle_background_image:
            return mark_safe(f'<img src = "{obj.middle_background_image.url}" width="100%" height="500px"/>')
        return '-'

    top_background_image_preview.short_description = 'Предпросмотр главного изображения'
    middle_background_image_preview.short_description = 'Предпросмотр изображения среднего блока'
