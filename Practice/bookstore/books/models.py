from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return "<Author id={} name={}>".format(self.id, self.name)


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, blank=True, null=True, related_name="books"
    )
    title = models.CharField(max_length=300)
    isbn = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    pub_year = models.PositiveIntegerField("publication year")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return "<Book id={} title={} year={}>".format(
            self.id, self.title, self.pub_year,
        )
