from django.contrib import admin

from .models import Author, Category, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ("name", "slug", "created_at")

    prepopulated_fields = {"slug": ["name"]}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    search_fields = ("title", "description", "author__name")

    list_display = ("title", "author", "category", "isbn", "pub_year", "created_at")
    list_filter = ("pub_year", "created_at")
    list_select_related = ("author", "category")
    
    ordering = ("title",)
    
    readonly_fields = ("created_at", "updated_at")
