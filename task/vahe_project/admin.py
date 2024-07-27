from django.contrib import admin
from django.utils.html import format_html
from .models import Lesson, Categories


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_per_month', 'lessons_count', 'team_lead', 'image_thumbnail')

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return 'No Image'
    image_thumbnail.short_description = 'Image'

    list_display_links = ('title',)
    list_editable = ('price_per_month', 'lessons_count', 'team_lead')
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ()
    fieldsets = (
        ('Main Information', {'fields': (
            ('title', 'slug',),
            ('price_per_month',),
            ('lessons_count', 'lessons_duration', 'pupils_count'),
            ('description',)
        )}),
        ('Optional info', {'fields': (
            ('company_address', 'support_phone_number'),
            ('team_lead', 'team_lead_name',),
            'category',
            'image',
        )}),
        ('Permissions', {'fields': (
            'start_date',
            ('status',),
        )}),
    )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')


