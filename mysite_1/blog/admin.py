from django.contrib import admin
from .models import post
# Register your models here.
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'published',
        'status',
    )
    list_filter = (
        'status',
        'created',
        'published',
        'author',
    )
    search_fields = (
        'title',
        'body',
    )
    prepopulated_fields  = {
        'slug': ('title',)
    }
    date_hierarchy = 'published'
    ordering = (
        '-status',
        '-published'
    )
