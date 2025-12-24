"""Admin configuration for blog app."""

from django.contrib import admin

from .models import Category, Comment, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'location',
        'author',
        'is_published',
        'pub_date',
        'created_at',
    )
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'text')
    list_select_related = ('category', 'location', 'author')
    raw_id_fields = ('author',)
    date_hierarchy = 'pub_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'text_preview')
    list_filter = ('created_at',)
    search_fields = ('text', 'author__username', 'post__title')
    raw_id_fields = ('author', 'post')

    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Превью текста'
