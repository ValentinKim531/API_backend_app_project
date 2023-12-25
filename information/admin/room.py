from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from ..models import RoomImage, Room


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.room_image:
            return mark_safe(f'<img src = "{obj.room_image.url}" width="250px" height="350px"/>')
        return '-'

    image_preview.short_description = 'Предпросмотр изображения'


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    inlines = [RoomImageInline]
    fields = (
        'title','title_kz','title_en',
        'subtitle','subtitle_kz','subtitle_en',
        'description','description_kz','description_en',
        'available','price'
    )
