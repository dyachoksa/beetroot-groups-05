from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Author, Category, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ("name", "slug", "list_thumbnail", "created_at")
    list_display_links = ("name", "slug")
    list_filter = ("created_at",)

    prepopulated_fields = {"slug": ["name"]}

    list_thumbnail = AdminThumbnail(image_field='admin_thumbnail')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ("name", "slug", "created_at")

    prepopulated_fields = {"slug": ["name"]}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    search_fields = ("title", "description", "author__name")

    list_display = (
        "title", 
        "slug", 
        "author", 
        "category", 
        "pub_year", 
        "num_views", 
        "list_thumbnail", 
        "is_featured",
        "created_at",
    )
    list_display_links = ("title", "slug")
    list_filter = ("is_featured", "pub_year", "created_at")
    list_select_related = ("author", "category")
    
    ordering = ("title",)

    prepopulated_fields = {"slug": ["title"]}
    
    readonly_fields = ("created_at", "updated_at")

    list_thumbnail = AdminThumbnail(image_field='admin_thumbnail')
