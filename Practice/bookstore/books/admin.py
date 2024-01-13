from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    search_fields = ("title", "description", "author__name")

    list_display = ("title", "author", "isbn", "pub_year", "created_at")
    list_filter = ("pub_year", "created_at")
    list_select_related = ("author",)
    
    ordering = ("title",)
    
    readonly_fields = ("created_at", "updated_at")
