from django.contrib import admin
from .models import News, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'news'
    model = Gallery
    readonly_fields = ['image_img']

    def image_img(self, obj):
        from django.utils.safestring import mark_safe
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="60"')
        else:
            print("No image assigned to object")

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ['publication_date']
    list_display = ['headers', 'body_news']
    fields = ['headers', 'body_news']
    inlines = [GalleryInline]

