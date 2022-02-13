from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Image, Place


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ('place', 'position')


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'get_preview', 'position']
    extra = 1
    readonly_fields = ('get_preview',)

    def get_preview(self, preview_image):
        return mark_safe(
            f'<img src="{preview_image.image.url}" width=300 height=200 />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
