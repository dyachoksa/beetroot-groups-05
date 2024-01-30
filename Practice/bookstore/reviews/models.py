from django.conf import settings
from django.db import models


class Review(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content[:50]
    
    def __repr__(self) -> str:
        return "<Review id={} book={} user={}>".format(
            self.id, self.book_id, self.user_id
        )
