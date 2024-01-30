from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    list_display = ("pk", "book", "user", "created_at")
    list_filter = ("created_at",)
    list_select_related = ("book", "user")
