from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from ..models import SocialNetwork, Contact


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    inlines = [SocialNetworkInline]
    fields = (
        'address','address_kz','address_en',
        'phone','email'
    )

    def has_add_permission(self, request):
        count = self.model.objects.count()
        max_objects = 1
        if count >= max_objects:
            return False
        else:
            return True
