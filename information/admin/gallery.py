from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from ..models import GalleryImage, Gallery


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.gallery_image:
            return mark_safe(f'<img src = "{obj.gallery_image.url}" width="250px" height="350px"/>')
        return '-'

    image_preview.short_description = 'Предпросмотр изображения'


@admin.register(Gallery)
class GalleryAdmin(SummernoteModelAdmin):
    inlines = [GalleryImageInline]
    fields = (
        'title','title_kz','title_en',
        'subtitle','subtitle_kz','subtitle_en'
    )

    def has_add_permission(self, request):
        count = self.model.objects.count()
        max_objects = 1
        if count >= max_objects:
            return False
        else:
            return True
