from django.contrib import admin
from .models import Post, comment
# Register your models here.
@admin.register(Post)
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

@admin.register(comment)    
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'post',
        'created',
        'active',
    ]
    list_filter = [
        'name',
        'email',
        'body',
    ]

