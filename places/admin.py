from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Image, Place


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ('place', 'position')


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'position')

    def get_preview(self, preview_image):
        return mark_safe(
            f'<img src="{preview_image.image.url}" width=300 height=200 />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
