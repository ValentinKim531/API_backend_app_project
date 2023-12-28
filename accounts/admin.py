from django.contrib import admin
from django.utils.html import mark_safe

from .models import User, OTP


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        'avatar', 'avatar_preview', 'username',
        'password', 'last_name', 'first_name', 'phone_number',
        'is_staff', 'is_active'
    )
    list_display = ('username', 'last_name', 'first_name', 'phone_number')
    readonly_fields = ('avatar_preview',)
    list_per_page = 15

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj and 'avatar_preview' not in self.readonly_fields:
            self.readonly_fields += ('avatar_preview',)
        return fieldsets

    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" width="250" height="250"/>'
            )
        return 'Аватар отсуствует'

    avatar_preview.short_description = 'Превью аватара'


admin.site.register(OTP)


