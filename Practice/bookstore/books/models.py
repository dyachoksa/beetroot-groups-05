from django.db import models
from django.urls import reverse


class Author(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to="authors/photos")
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return "<Author id={} name={}>".format(self.id, self.name)
    
    def get_absolute_url(self):
        return reverse("books_author", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to="books/categories")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return "<Category id={} name={} slug={}>".format(
            self.pk, self.name, self.slug
        )
    
    def get_absolute_url(self):
        return reverse("books_category", kwargs={"slug": self.slug})


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, blank=True, null=True, related_name="books"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=False, related_name="books"
    )
    image = models.ImageField(blank=True, null=True, upload_to="books/images/%Y")
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
    
    def get_absolute_url(self):
        return reverse("books_detail", kwargs={"pk": self.pk})
