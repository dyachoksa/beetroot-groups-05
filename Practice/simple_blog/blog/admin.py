from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

    search_fields = ('title', 'short_content')

    list_display = ['title', 'slug', 'published_at', 'created_at']

    list_filter = ('published_at', 'created_at')
